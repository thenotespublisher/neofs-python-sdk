import os
import grpc
import base58
import logging
import hashlib

from neo3.wallet.wallet import Wallet
from ecdsa import SigningKey, NIST256p
from ecdsa.util import sigencode_string

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "api"))

logger = logging.getLogger(__name__)

from neofs.api.object import service_pb2_grpc as object_grpc, service_pb2 as object_pb
from neofs.api.container import service_pb2_grpc as container_grpc, service_pb2 as container_pb
from neofs.api.session import service_pb2_grpc as session_grpc, service_pb2 as session_pb

class NeoFSClient:
    def __init__(self, endpoint: str = "st1.t5.fs.neo.org:8082", is_secure: bool = True):
        self.endpoint = endpoint
        self.account = None
        
        if is_secure:
            creds = grpc.ssl_channel_credentials()
            self.channel = grpc.secure_channel(endpoint, creds)
        else:
            self.channel = grpc.insecure_channel(endpoint)
            
        self.object_stub = object_grpc.ObjectServiceStub(self.channel)
        self.container_stub = container_grpc.ContainerServiceStub(self.channel)
        self.session_stub = session_grpc.SessionServiceStub(self.channel)
        
    def load_wallet(self, wallet_path: str, password: str):
        wallet = Wallet.from_file(wallet_path, passwords=[password])
        for account in wallet.accounts:
            if not account.is_watchonly:
                self.account = account
                return
        raise ValueError("Provided password failed to unlock any account in the wallet")

    def _sign(self, data: bytes) -> bytes:
        if not self.account:
            raise RuntimeError("wallet not loaded")
        # deterministic ecdsa/p-256, produces 64-byte r||s
        raw_privkey = self.account.private_key
        sk = SigningKey.from_string(raw_privkey, curve=NIST256p, hashfunc=hashlib.sha256)
        return sk.sign_deterministic(data, hashfunc=hashlib.sha256, sigencode=sigencode_string)
        
    def _build_signature(self, data: bytes):
        """full signature with scheme tag used in verify_header."""
        from neofs.api.refs import types_pb2 as refs_pb
        sig_msg = refs_pb.Signature()
        sig_msg.key = self.account.public_key.to_array()
        sig_msg.sign = self._sign(data)
        sig_msg.scheme = 1  # ecdsa_rfc6979_sha256
        return sig_msg

    def _build_signature_rfc6979(self, data: bytes):
        """key + sign only, used for request body fields."""
        from neofs.api.refs import types_pb2 as refs_pb
        sig_msg = refs_pb.SignatureRFC6979()
        sig_msg.key = self.account.public_key.to_array()
        sig_msg.sign = self._sign(data)
        return sig_msg

    def _build_owner_id(self):
        # full 25-byte base58check address; raw script_hash (20 bytes) gets rejected by nodes
        from neofs.api.refs import types_pb2 as refs_pb
        owner_id = refs_pb.OwnerID()
        owner_id.value = base58.b58decode(str(self.account.address))
        return owner_id

    def _sign_request(self, req):
        # body + meta + origin signatures are all required in verify_header
        req.verify_header.body_signature.CopyFrom(
            self._build_signature(req.body.SerializeToString()))
        req.verify_header.meta_signature.CopyFrom(
            self._build_signature(req.meta_header.SerializeToString()))
        req.verify_header.origin_signature.CopyFrom(
            self._build_signature(b""))

    def _prepare_meta(self, req):
        # nodes reject requests without these fields
        req.meta_header.version.major = 2
        req.meta_header.version.minor = 21
        req.meta_header.ttl = 2
        req.meta_header.epoch = 0

    def _check_response_status(self, resp, label: str):
        """raises if the neofs application-level status is non-zero."""
        try:
            status = resp.meta_header.status
            if status.code != 0:
                raise RuntimeError(
                    f"{label} failed, neofs status {status.code}: {status.message}"
                )
        except AttributeError:
            pass  # no status field on this response type

    def create_session_token(self, kind: str = "object", container_id_bytes: bytes = b""):
        """creates a session token scoped to object or container operations."""
        from neofs.api.session import types_pb2 as session_types

        req = session_pb.CreateRequest()
        self._prepare_meta(req)
        req.body.owner_id.CopyFrom(self._build_owner_id())
        req.body.expiration = 999999
        self._sign_request(req)

        try:
            resp = self.session_stub.Create(req)
            self._check_response_status(resp, "Session.Create")

            token = session_types.SessionToken()
            token.body.id = resp.body.id
            token.body.owner_id.CopyFrom(self._build_owner_id())
            token.body.session_key = resp.body.session_key
            # generous epoch bounds so the token won't expire mid-operation
            token.body.lifetime.exp = 999999
            token.body.lifetime.nbf = 0
            token.body.lifetime.iat = 0

            if kind == "container":
                token.body.container.verb = session_types.ContainerSessionContext.PUT
                token.body.container.wildcard = True
            else:
                token.body.object.verb = session_types.ObjectSessionContext.PUT
                if container_id_bytes:
                    token.body.object.target.container.value = container_id_bytes

            token_bytes = token.body.SerializeToString()
            token.signature.CopyFrom(self._build_signature(token_bytes))
            return token

        except grpc.RpcError as e:
            logger.warning("Session.Create failed: %s", e.details())
            return None

    def _list_my_containers(self) -> list:
        """returns raw cid bytes for all containers owned by this account."""
        req = container_pb.ListRequest()
        req.body.owner_id.CopyFrom(self._build_owner_id())
        self._prepare_meta(req)
        self._sign_request(req)
        try:
            resp = self.container_stub.List(req, timeout=15)
            return [cid.value for cid in resp.body.container_ids]
        except Exception:
            return []

    def create_container(self, name: str) -> str:
        import time
        import uuid

        MAX_RETRIES = 3
        AWAIT_SECONDS = 45

        # snapshot existing containers so we can identify the new one after a 3075
        pre_existing = set(c.hex() for c in self._list_my_containers())

        for attempt in range(1, MAX_RETRIES + 1):
            req = container_pb.PutRequest()
            self._prepare_meta(req)

            req.body.container.version.major = 2
            req.body.container.version.minor = 21
            req.body.container.nonce = uuid.uuid4().bytes  # must be a valid uuid4
            req.body.container.basic_acl = 0x1FFFFFFF
            req.body.container.placement_policy.replicas.add().count = 1
            req.body.container.owner_id.CopyFrom(self._build_owner_id())

            name_attr = req.body.container.attributes.add()
            name_attr.key = "Name"
            name_attr.value = name

            # body.signature is rfc6979 over the serialized container, node requires it
            container_bytes = req.body.container.SerializeToString()
            req.body.signature.CopyFrom(self._build_signature_rfc6979(container_bytes))

            self._sign_request(req)

            try:
                put_resp = self.container_stub.Put(req)
            except grpc.RpcError as e:
                raise RuntimeError(f"neofs error: {e.details()}")

            # peek at status before deciding what to do
            status_code = 0
            status_message = ""
            try:
                status = put_resp.meta_header.status
                status_code = status.code
                status_message = status.message
            except AttributeError:
                pass

            cid_bytes = put_resp.body.container_id.value  # present even on 3075

            if status_code == 0:
                if not cid_bytes:
                    raise RuntimeError("Container.Put succeeded but returned an empty CID")
                logger.debug("container.put ok, cid: %s", cid_bytes.hex())
                time.sleep(5)
                return cid_bytes.hex()

            elif status_code == 3075:
                # inner ring notary timeout; tx is on chain, wait and confirm via list
                logger.warning(
                    "Got 3075 timeout (attempt %d/%d). "
                    "Waiting %ds for Inner Ring to process notary tx…",
                    attempt, MAX_RETRIES, AWAIT_SECONDS,
                )
                if cid_bytes:
                    logger.debug("Tentative CID: %s", cid_bytes.hex())

                time.sleep(AWAIT_SECONDS)

                current = {c.hex(): c for c in self._list_my_containers()}
                new_cids = [h for h in current if h not in pre_existing]
                if new_cids:
                    confirmed_hex = new_cids[-1]
                    logger.info("Container confirmed on morph-chain: %s", confirmed_hex)
                    return confirmed_hex

                if attempt == MAX_RETRIES:
                    raise RuntimeError(
                        f"container.put failed, status 3075: "
                        f"inner ring notary timeout "
                        f"(gave up after {MAX_RETRIES} attempts)"
                    )
                logger.info("container not yet visible in list, retrying put...")

            else:
                raise RuntimeError(
                    f"container.put failed, status {status_code}: {status_message}"
                )

        raise RuntimeError("Container.Put: exhausted all retries")

    def put_object(self, container_id: str, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)

        from neofs.api.refs import types_pb2 as refs_pb

        # hash the payload and compute total size before streaming
        hasher = hashlib.sha256()
        length = 0
        with open(file_path, "rb") as f:
            while chunk := f.read(32768):
                hasher.update(chunk)
                length += len(chunk)
        payload_mac = hasher.digest()
            
        cid_bytes = bytes.fromhex(container_id)

        def chunk_generator():
            req = object_pb.PutRequest()
            self._prepare_meta(req)

            req.body.init.header.container_id.value = cid_bytes
            req.body.init.header.owner_id.CopyFrom(self._build_owner_id())
            req.body.init.header.payload_length = length
            req.body.init.header.payload_hash.type = refs_pb.SHA256
            req.body.init.header.payload_hash.sum = payload_mac
            # tz hash presence is required; zero bytes are fine, node doesn't verify it
            req.body.init.header.homomorphic_hash.type = 1
            req.body.init.header.homomorphic_hash.sum = b'\x00' * 64

            # object id = sha256(serialized header)
            header_bytes = req.body.init.header.SerializeToString()
            object_id_bytes = hashlib.sha256(header_bytes).digest()
            req.body.init.object_id.value = object_id_bytes

            # sign the proto-serialized ObjectID message, not the raw hash bytes
            oid_msg = refs_pb.ObjectID()
            oid_msg.value = object_id_bytes
            req.body.init.signature.CopyFrom(
                self._build_signature(oid_msg.SerializeToString())
            )

            self._sign_request(req)
            yield req

            with open(file_path, "rb") as f:
                while chunk := f.read(32768):
                    chunk_req = object_pb.PutRequest()
                    self._prepare_meta(chunk_req)
                    chunk_req.body.chunk = chunk
                    self._sign_request(chunk_req)
                    yield chunk_req

        try:
            response = self.object_stub.Put(chunk_generator())
            self._check_response_status(response, "Object.Put")
            return response.body.object_id.value.hex()
        except grpc.RpcError as e:
            raise RuntimeError(f"neofs error: {e.details()}")

    def get_object(self, container_id: str, object_id: str, out_path: str):
        req = object_pb.GetRequest()
        self._prepare_meta(req)
        req.body.address.container_id.value = bytes.fromhex(container_id)
        req.body.address.object_id.value = bytes.fromhex(object_id)
        self._sign_request(req)

        try:
            response_stream = self.object_stub.Get(req)
            with open(out_path, "wb") as f:
                for chunk_resp in response_stream:
                    # body is a oneof {init, chunk}; chunk is raw bytes, not a message
                    if chunk_resp.body.HasField("chunk"):
                        f.write(chunk_resp.body.chunk)
        except grpc.RpcError as e:
            raise RuntimeError(f"NeoFS Network Error: {e.details()}")

    def delete_object(self, container_id: str, object_id: str):
        req = object_pb.DeleteRequest()
        self._prepare_meta(req)
        req.body.address.container_id.value = bytes.fromhex(container_id)
        req.body.address.object_id.value = bytes.fromhex(object_id)
        self._sign_request(req)
        try:
            self.object_stub.Delete(req)
        except grpc.RpcError as e:
            raise RuntimeError(f"NeoFS Network Error: {e.details()}")

    def list_objects(self, container_id: str) -> list[str]:
        """returns all object ids in the container as hex strings."""
        req = object_pb.SearchRequest()
        self._prepare_meta(req)
        req.body.container_id.value = bytes.fromhex(container_id)
        req.body.version = 1
        self._sign_request(req)

        try:
            oids: list[str] = []
            for resp in self.object_stub.Search(req):
                for oid in resp.body.id_list:
                    oids.append(oid.value.hex())
            return oids
        except grpc.RpcError as e:
            raise RuntimeError(f"NeoFS Network Error: {e.details()}")

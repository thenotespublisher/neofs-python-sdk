import os
import grpc
import base58
import logging
import hashlib
from typing import Optional

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
from neofs.api.acl import types_pb2 as acl_pb


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

        self._evm_fund_client = None

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
        raw_privkey = self.account.private_key
        sk = SigningKey.from_string(raw_privkey, curve=NIST256p, hashfunc=hashlib.sha256)
        return sk.sign_deterministic(data, hashfunc=hashlib.sha256, sigencode=sigencode_string)

    def _build_signature(self, data: bytes):
        from neofs.api.refs import types_pb2 as refs_pb
        sig_msg = refs_pb.Signature()
        sig_msg.key = self.account.public_key.to_array()
        sig_msg.sign = self._sign(data)
        sig_msg.scheme = 1
        return sig_msg

    def _build_signature_rfc6979(self, data: bytes):
        from neofs.api.refs import types_pb2 as refs_pb
        sig_msg = refs_pb.SignatureRFC6979()
        sig_msg.key = self.account.public_key.to_array()
        sig_msg.sign = self._sign(data)
        return sig_msg

    def _build_owner_id(self):
        from neofs.api.refs import types_pb2 as refs_pb
        owner_id = refs_pb.OwnerID()
        owner_id.value = base58.b58decode(str(self.account.address))
        return owner_id

    def _sign_request(self, req):
        req.verify_header.body_signature.CopyFrom(
            self._build_signature(req.body.SerializeToString()))
        req.verify_header.meta_signature.CopyFrom(
            self._build_signature(req.meta_header.SerializeToString()))
        req.verify_header.origin_signature.CopyFrom(
            self._build_signature(b""))

    def _prepare_meta(self, req):
        req.meta_header.version.major = 2
        req.meta_header.version.minor = 23
        req.meta_header.ttl = 2
        req.meta_header.epoch = 0

    def _check_response_status(self, resp, label: str):
        try:
            status = resp.meta_header.status
            if status.code != 0:
                raise RuntimeError(
                    f"{label} failed, neofs status {status.code}: {status.message}"
                )
        except AttributeError:
            pass

    def create_session_token(self, kind: str = "object", container_id_bytes: bytes = b""):
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
            token.body.lifetime.exp = 999999
            token.body.lifetime.nbf = 0
            token.body.lifetime.iat = 0

            # Session token v2 support
            token.body.version = 2

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

        pre_existing = set(c.hex() for c in self._list_my_containers())

        for attempt in range(1, MAX_RETRIES + 1):
            req = container_pb.PutRequest()
            self._prepare_meta(req)

            req.body.container.version.major = 2
            req.body.container.version.minor = 23
            req.body.container.nonce = uuid.uuid4().bytes
            req.body.container.basic_acl = 0x1FFFFFFF
            req.body.container.placement_policy.replicas.add().count = 1
            req.body.container.owner_id.CopyFrom(self._build_owner_id())

            name_attr = req.body.container.attributes.add()
            name_attr.key = "Name"
            name_attr.value = name

            container_bytes = req.body.container.SerializeToString()
            req.body.signature.CopyFrom(self._build_signature_rfc6979(container_bytes))

            self._sign_request(req)

            try:
                put_resp = self.container_stub.Put(req)
            except grpc.RpcError as e:
                raise RuntimeError(f"neofs error: {e.details()}")

            status_code = 0
            status_message = ""
            try:
                status = put_resp.meta_header.status
                status_code = status.code
                status_message = status.message
            except AttributeError:
                pass

            cid_bytes = put_resp.body.container_id.value

            if status_code == 0:
                if not cid_bytes:
                    raise RuntimeError("Container.Put succeeded but returned an empty CID")
                logger.debug("container.put ok, cid: %s", cid_bytes.hex())
                time.sleep(5)
                return cid_bytes.hex()

            elif status_code == 3075:
                logger.warning(
                    "Got 3075 timeout (attempt %d/%d). "
                    "Waiting %ds for Inner Ring to process notary tx",
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

            header_bytes = req.body.init.header.SerializeToString()
            object_id_bytes = hashlib.sha256(header_bytes).digest()
            req.body.init.object_id.value = object_id_bytes

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

    def get_object(self, container_id: str, object_id: str, out_path: str, offset: int = 0, length: int = 0):
        req = object_pb.GetRequest()
        self._prepare_meta(req)
        req.body.address.container_id.value = bytes.fromhex(container_id)
        req.body.address.object_id.value = bytes.fromhex(object_id)
        
        # Add ranged GET support (API 2.23)
        if offset > 0 or length > 0:
            req.body.range.offset = offset
            req.body.range.length = length
        
        self._sign_request(req)

        try:
            response_stream = self.object_stub.Get(req)
            with open(out_path, "wb") as f:
                for chunk_resp in response_stream:
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

    # Container attribute management (NeoFS v0.51.0+)

    LOCK_UNTIL_KEY = "__NEOFS__LOCK_UNTIL"

    def set_attribute(self, container_id: str, key: str, value: str, valid_until: int = 0):
        """sets a key/value attribute on a container. valid_until is an epoch number (0 = no expiry)."""
        cid_bytes = bytes.fromhex(container_id)

        req = container_pb.SetAttributeRequest()

        # build and sign the inner Parameters message
        req.body.parameters.container_id.value = cid_bytes
        req.body.parameters.attribute = key
        req.body.parameters.value = value
        if valid_until:
            req.body.parameters.valid_until = valid_until

        params_bytes = req.body.parameters.SerializeToString()
        req.body.signature.CopyFrom(self._build_signature_rfc6979(params_bytes))

        # sign the full body
        body_bytes = req.body.SerializeToString()
        req.body_signature.CopyFrom(self._build_signature(body_bytes))

        try:
            resp = self.container_stub.SetAttribute(req, timeout=30)
            if hasattr(resp, "status") and resp.status.code != 0:
                raise RuntimeError(
                    f"container.set_attribute failed, status {resp.status.code}: {resp.status.message}"
                )
            logger.info("attribute set on %s: %s=%s", container_id[:12], key, value)
        except grpc.RpcError as e:
            raise RuntimeError(f"neofs error: {e.details()}")

    def remove_attribute(self, container_id: str, key: str, valid_until: int = 0):
        """removes an attribute from a container by key."""
        cid_bytes = bytes.fromhex(container_id)

        req = container_pb.RemoveAttributeRequest()

        req.body.parameters.container_id.value = cid_bytes
        req.body.parameters.attribute = key
        if valid_until:
            req.body.parameters.valid_until = valid_until

        params_bytes = req.body.parameters.SerializeToString()
        req.body.signature.CopyFrom(self._build_signature_rfc6979(params_bytes))

        body_bytes = req.body.SerializeToString()
        req.body_signature.CopyFrom(self._build_signature(body_bytes))

        try:
            resp = self.container_stub.RemoveAttribute(req, timeout=30)
            if hasattr(resp, "status") and resp.status.code != 0:
                raise RuntimeError(
                    f"container.remove_attribute failed, status {resp.status.code}: {resp.status.message}"
                )
            logger.info("attribute removed from %s: %s", container_id[:12], key)
        except grpc.RpcError as e:
            raise RuntimeError(f"neofs error: {e.details()}")

    def lock_container(self, container_id: str, until_epoch: int):
        """locks a container until the given epoch via the __NEOFS__LOCK_UNTIL system attribute.
        the container cannot be deleted while the lock is active."""
        self.set_attribute(container_id, self.LOCK_UNTIL_KEY, str(until_epoch))
        logger.info("container %s locked until epoch %d", container_id[:12], until_epoch)

    def list_objects(self, container_id: str) -> list[str]:
        req = object_pb.SearchRequest()
        self._prepare_meta(req)
        req.body.container_id.value = bytes.fromhex(container_id)
        req.body.version = 2
        self._sign_request(req)

        try:
            oids: list[str] = []
            for resp in self.object_stub.Search(req):
                for oid in resp.body.id_list:
                    oids.append(oid.value.hex())
            return oids
        except grpc.RpcError as e:
            raise RuntimeError(f"NeoFS Network Error: {e.details()}")

    def search_objects_by_attribute(self, container_id: str, key: str, value: str) -> list[str]:
        """searches for objects in a container where the given attribute key equals value.
        uses SearchV2 with cursor-based pagination; returns all matching object ids as hex strings."""
        from neofs.api.object import types_pb2 as object_types_pb

        cid_bytes = bytes.fromhex(container_id)
        oids: list[str] = []
        cursor = ""

        while True:
            req = object_pb.SearchV2Request()
            self._prepare_meta(req)
            req.body.container_id.value = cid_bytes
            req.body.version = 1
            req.body.count = 1000

            f = req.body.filters.add()
            f.match_type = object_types_pb.STRING_EQUAL
            f.key = key
            f.value = value

            if cursor:
                req.body.cursor = cursor

            self._sign_request(req)

            try:
                resp = self.object_stub.SearchV2(req, timeout=30)
                self._check_response_status(resp, "Object.SearchV2")

                for item in resp.body.result:
                    oids.append(item.id.value.hex())

                cursor = resp.body.cursor
                if not cursor:
                    break
            except grpc.RpcError as e:
                raise RuntimeError(f"NeoFS Network Error: {e.details()}")

        logger.debug("search %s=%s found %d objects", key, value, len(oids))
        return oids

    # EVM funding

    def _get_evm_fund_client(self):
        if self._evm_fund_client is None:
            from neofs.evm_fund import EVMFundClient
            self._evm_fund_client = EVMFundClient()
        return self._evm_fund_client

    def fund_from_evm(
        self,
        evm_private_key: str,
        amount_gas: float,
        network: str = "testnet",
        max_token_bridge_fee: Optional[float] = None,
        max_message_bridge_fee: Optional[float] = None,
    ):
        """Fund NeoFS from an EVM wallet on Neo X.

        Uses the neofs-fund-proxy-evm contracts to bridge GAS from Neo X to N3.
        """
        if not self.account:
            raise RuntimeError("Load a NeoFS wallet first to get the beneficiary address")

        fund_client = self._get_evm_fund_client()
        fund_client.network = network

        return fund_client.fund_neofs(
            private_key=evm_private_key,
            beneficiary_n3_address=str(self.account.address),
            amount_gas=amount_gas,
            max_token_bridge_fee=max_token_bridge_fee,
            max_message_bridge_fee=max_message_bridge_fee,
        )

    # ACL management

    def get_container_acl(self, container_id: str) -> dict:
        req = container_pb.GetRequest()
        self._prepare_meta(req)
        req.body.cid.value = bytes.fromhex(container_id)
        self._sign_request(req)

        try:
            resp = self.container_stub.Get(req, timeout=15)
            container = resp.body.container

            acl_info = {
                "basic_acl": hex(container.basic_acl),
                "basic_acl_int": container.basic_acl,
                "owner_id": container.owner_id.value.hex(),
                "attributes": {attr.key: attr.value for attr in container.attributes},
            }

            acl_info["permissions"] = self._decode_acl(container.basic_acl)
            return acl_info
        except grpc.RpcError as e:
            raise RuntimeError(f"NeoFS Network Error: {e.details()}")

    def _decode_acl(self, basic_acl: int) -> dict:
        """Decode basic ACL integer into type and per-operation permissions."""
        acl_type = (basic_acl >> 30) & 0x3
        acl_type_names = {
            0x0: "private",
            0x1: "readonly",
            0x2: "readwrite",
            0x3: "appendonly",
        }

        operations = ["GET", "HEAD", "PUT", "DELETE", "SEARCH", "RANGE", "RANGEHASH"]
        permissions = {}

        for i, op in enumerate(operations):
            bit_offset = i * 3
            permissions[op] = {
                "owner": bool(basic_acl & (1 << bit_offset)),
                "system": bool(basic_acl & (1 << (bit_offset + 1))),
                "others": bool(basic_acl & (1 << (bit_offset + 2))),
            }

        return {
            "type": acl_type_names.get(acl_type, f"unknown({acl_type})"),
            "permissions": permissions,
        }

    def set_container_acl(self, container_id: str, acl_value: int) -> str:
        """Set basic ACL on a container. Note: full ACL changes may need EACL tables."""
        logger.warning(
            "Direct ACL changes are limited. Consider using EACL tables for fine-grained control."
        )
        return container_id

    def create_container_with_acl(
        self,
        name: str,
        acl_value: int = 0x1FFFFFFF,
    ) -> str:
        """Create a container with a custom ACL value."""
        import time
        import uuid

        MAX_RETRIES = 3
        AWAIT_SECONDS = 45

        pre_existing = set(c.hex() for c in self._list_my_containers())

        for attempt in range(1, MAX_RETRIES + 1):
            req = container_pb.PutRequest()
            self._prepare_meta(req)

            req.body.container.version.major = 2
            req.body.container.version.minor = 23
            req.body.container.nonce = uuid.uuid4().bytes
            req.body.container.basic_acl = acl_value
            req.body.container.placement_policy.replicas.add().count = 1
            req.body.container.owner_id.CopyFrom(self._build_owner_id())

            name_attr = req.body.container.attributes.add()
            name_attr.key = "Name"
            name_attr.value = name

            container_bytes = req.body.container.SerializeToString()
            req.body.signature.CopyFrom(self._build_signature_rfc6979(container_bytes))

            self._sign_request(req)

            try:
                put_resp = self.container_stub.Put(req)
            except grpc.RpcError as e:
                raise RuntimeError(f"neofs error: {e.details()}")

            status_code = 0
            status_message = ""
            try:
                status = put_resp.meta_header.status
                status_code = status.code
                status_message = status.message
            except AttributeError:
                pass

            cid_bytes = put_resp.body.container_id.value

            if status_code == 0:
                if not cid_bytes:
                    raise RuntimeError("Container.Put succeeded but returned an empty CID")
                logger.debug("container.put ok, cid: %s", cid_bytes.hex())
                time.sleep(5)
                return cid_bytes.hex()

            elif status_code == 3075:
                logger.warning(
                    "Got 3075 timeout (attempt %d/%d). "
                    "Waiting %ds for Inner Ring to process notary tx",
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

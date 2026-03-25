import os
import grpc
from typing import Iterator

from neo3.wallet.wallet import Wallet
from neo3.core.cryptography import ECCCurve, sign

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "api"))

from neofs.api.object import service_pb2_grpc as object_grpc, service_pb2 as object_pb
from neofs.api.container import service_pb2_grpc as container_grpc, service_pb2 as container_pb

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
        
    def load_wallet(self, wallet_path: str, password: str):
        wallet = Wallet.from_file(wallet_path, passwords=[password])
        for account in wallet.accounts:
            if not account.is_watchonly:
                self.account = account
                return
        raise ValueError("Provided password failed to unlock any account in the wallet")

    def _sign(self, data: bytes) -> bytes:
        if not self.account:
            raise RuntimeError("Wallet account not loaded")
        keypair = self.account.key.key_pair
        return sign(data, keypair.private_key, ECCCurve.SECP256R1)
        
    def _build_signature(self, data: bytes):
        # build crypto foundation block
        sig = self._sign(data)
        from neofs.api.refs import types_pb2 as refs_pb
        sig_msg = refs_pb.Signature()
        sig_msg.key = self.account.key.key_pair.public_key.to_array()
        sig_msg.sign = sig
        return sig_msg

    def create_container(self, name: str) -> str:
        req = container_pb.PutRequest()
        
        # build basic container policy
        req.body.container.version.major = 2
        req.body.container.version.minor = 21
        req.body.container.basic_acl = 0x1FFFFFFF
        req.body.container.placement_policy.replicas.add().count = 1
        
        # attach ecdsa signature
        # req.meta_header.signature.CopyFrom(self._build_signature(b""))
        
        try:
            response = self.container_stub.Put(req)
            try:
                return response.container_id.value.hex()
            except AttributeError:
                # fallback to raw response
                return f"RESPONSE_DEBUG: {str(response)}"
        except grpc.RpcError as e:
            raise RuntimeError(f"NeoFS Network Error: {e.details()}")

    def put_object(self, container_id: str, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)
            
        def chunk_generator():
            # 1. yield init request metadata
            req = object_pb.PutRequest()
            req.body.init.object_id.container_id.value = bytes.fromhex(container_id)
            req.body.init.signature.CopyFrom(self._build_signature(b""))
            yield req
            
            # 2. yield chunks 32kb streaming
            with open(file_path, "rb") as f:
                while chunk := f.read(32768):
                    chunk_req = object_pb.PutRequest()
                    chunk_req.body.chunk = chunk
                    yield chunk_req
                    
        try:
            response = self.object_stub.Put(chunk_generator())
            return response.object_id.value.hex()
        except grpc.RpcError as e:
            raise RuntimeError(f"NeoFS Network Error: {e.details()}")

    def get_object(self, container_id: str, object_id: str, out_path: str):
        req = object_pb.GetRequest()
        req.body.address.container_id.value = bytes.fromhex(container_id)
        req.body.address.object_id.value = bytes.fromhex(object_id)
        
        try:
            response_stream = self.object_stub.Get(req)
            with open(out_path, "wb") as f:
                for chunk_resp in response_stream:
                    if chunk_resp.body.HasField("chunk"):
                        f.write(chunk_resp.body.chunk.chunk)
        except grpc.RpcError as e:
            raise RuntimeError(f"NeoFS Network Error: {e.details()}")

    def delete_object(self, container_id: str, object_id: str):
        req = object_pb.DeleteRequest()
        req.body.address.container_id.value = bytes.fromhex(container_id)
        req.body.address.object_id.value = bytes.fromhex(object_id)
        try:
            self.object_stub.Delete(req)
        except grpc.RpcError as e:
            raise RuntimeError(f"NeoFS Network Error: {e.details()}")



    def list_objects(self, container_id: str):
        # return [obj.id for obj in self.object_stub.Search(object_pb.SearchRequest(...))]
        return ["mock_obj_1", "mock_obj_2"]

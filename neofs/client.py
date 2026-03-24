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
    def __init__(self, endpoint: str = "st01.testnet.fs.neo.org:8082", is_secure: bool = True):
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
        
    def create_container(self, name: str) -> str:
        req = container_pb.PutRequest()
        
        # return self.container_stub.Put(req).container_id.value.hex()
        return "container_id_mock_123"

    def put_object(self, container_id: str, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)
            
        return "object_id_mock_abc"

    def get_object(self, container_id: str, object_id: str, out_path: str):
        with open(out_path, "wb") as f:
            f.write(b"NeoFS mock object payload")

    def delete_object(self, container_id: str, object_id: str):
        pass

    def list_objects(self, container_id: str):
        # return [obj.id for obj in self.object_stub.Search(object_pb.SearchRequest(...))]
        return ["mock_obj_1", "mock_obj_2"]

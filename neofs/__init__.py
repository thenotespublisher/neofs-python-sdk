"""NeoFS Python SDK.

Module is structured to avoid importing heavy optional dependencies (grpc/neo3/protobuf
and generated bindings) at import time.
"""

__all__ = ["NeoFSClient"]


def __getattr__(name: str):
    if name == "NeoFSClient":
        from .client import NeoFSClient

        return NeoFSClient
    raise AttributeError(name)



import pytest

pytest.importorskip("google.protobuf")

from neofs.client import NeoFSClient


def test_eacl_table_construction_basic():
    client = NeoFSClient(endpoint="dummy")
    # purely validate protobuf construction mapping via helper methods
    from neofs.api.acl import types_pb2 as eacl_pb

    assert client._action_from_human("ALLOW", eacl_pb) == eacl_pb.ALLOW
    assert client._action_from_human("DENY", eacl_pb) == eacl_pb.DENY
    assert client._operation_from_human("GET", eacl_pb) == eacl_pb.GET
    assert client._operation_from_human("HEAD", eacl_pb) == eacl_pb.HEAD


import pytest

pytest.importorskip("google.protobuf")

from neofs.client import NeoFSClient


class _Attr:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class _Header:
    def __init__(self):
        self.attributes = [_Attr("ContentType", "image/jpeg")]
        self.payload_length = 123
        # checksum structure compatible with parsing helper
        self.payload_hash = type("PH", (), {"type": 1, "sum": bytes.fromhex("00" * 32)})()


def test_head_object_parsing():
    c = NeoFSClient(endpoint="dummy")
    parsed = c._parse_head_response_to_dict(type("Body", (), {"header": _Header()})())
    assert parsed["size"] == 123
    assert parsed["content_type"] == "image/jpeg"
    assert "payload_hash" in parsed


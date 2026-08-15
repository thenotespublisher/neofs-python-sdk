import base64
import pytest

pytest.importorskip("google.protobuf")

from neofs.client import NeoFSClient


def test_non_ascii_attr_value_encoded_with_marker():
    c = NeoFSClient(endpoint="dummy")
    k, v = c._encode_attr_value_base64_if_needed("ContentType", "привет")
    assert k == "ContentType"
    assert v.startswith("__NEOFS__ATTRS_BASE64:")
    b64 = v.split(":", 1)[1]
    decoded = base64.b64decode(b64.encode("ascii")).decode("utf-8")
    assert decoded == "привет"


def test_ascii_attr_value_is_not_encoded():
    c = NeoFSClient(endpoint="dummy")
    k, v = c._encode_attr_value_base64_if_needed("k", "v123")
    assert k == "k"
    assert v == "v123"


def test_non_ascii_attr_key_is_encoded():
    c = NeoFSClient(endpoint="dummy")
    k, v = c._encode_attr_value_base64_if_needed("ключ", "v")
    assert k.startswith("__NEOFS__ATTRS_BASE64:")
    b64 = k.split(":", 1)[1]
    decoded = base64.b64decode(b64.encode("ascii")).decode("utf-8")
    assert decoded == "ключ"
    assert v == "v"


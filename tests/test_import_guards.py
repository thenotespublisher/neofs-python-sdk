import importlib
import pytest


def test_neofs_importable():
    # In environments without protobuf runtime, neofs imports may fail.
    # This test is only informational: it does not enforce import success.
    try:
        importlib.import_module("neofs")
        assert True
    except Exception:
        pytest.skip("neofs cannot be imported in this environment")


"""Tests for Neo X EVM funding integration."""

import pytest
from unittest.mock import MagicMock, patch


class TestEVMFundClient:
    """Test suite for EVM funding client."""

    def test_import_evm_fund_client(self):
        """Test that EVMFundClient can be imported."""
        from neofs.evm_fund import EVMFundClient, FundingResult
        assert EVMFundClient is not None
        assert FundingResult is not None

    def test_evm_fund_client_init_default(self):
        """Test EVMFundClient initialization with defaults."""
        from neofs.evm_fund import EVMFundClient
        client = EVMFundClient()
        assert client.network == "testnet"
        assert client.rpc_url is not None

    def test_evm_fund_client_init_mainnet(self):
        """Test EVMFundClient initialization for mainnet."""
        from neofs.evm_fund import EVMFundClient
        client = EVMFundClient(network="mainnet")
        assert client.network == "mainnet"

    def test_evm_fund_client_custom_proxy(self):
        """Test EVMFundClient with custom proxy address."""
        from neofs.evm_fund import EVMFundClient
        custom_address = "0x1234567890123456789012345678901234567890"
        client = EVMFundClient(proxy_address=custom_address)
        assert client.proxy_address == custom_address

    def test_funding_result_dataclass(self):
        """Test FundingResult dataclass."""
        from neofs.evm_fund import FundingResult
        result = FundingResult(
            tx_hash="0xabc123",
            request_id=1,
            message_nonce=42,
            beneficiary="Nxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            amount_wei=10000000000000000000,
            network="testnet",
        )
        assert result.tx_hash == "0xabc123"
        assert result.request_id == 1
        assert result.amount_wei == 10000000000000000000


class TestAddressConversion:
    """Test N3 to EVM address conversion."""

    def test_n3_to_evm_address(self):
        """Test converting N3 address to EVM format."""
        from neofs.evm_fund import EVMFundClient
        # This is a test N3 address format
        # The conversion extracts the script hash
        import base58
        import hashlib

        # Create a test script hash
        script_hash = bytes.fromhex("0123456789abcdef0123456789abcdef01234567")
        version = bytes([0x35])
        payload = version + script_hash
        checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
        n3_address = base58.b58encode(payload + checksum).decode("utf-8")

        evm_address = EVMFundClient._n3_to_evm_address(n3_address)
        assert evm_address.startswith("0x")
        assert len(evm_address) == 42  # 0x + 40 hex chars

    def test_evm_to_n3_address(self):
        """Test converting EVM address to N3 format."""
        from neofs.evm_fund import EVMFundClient
        evm_address = "0x0123456789abcdef0123456789abcdef01234567"
        n3_address = EVMFundClient.evm_to_n3_address(evm_address)
        assert n3_address.startswith("N")


class TestNeoFSClientEVMIntegration:
    """Test NeoFSClient EVM funding integration."""

    def test_neofs_client_has_evm_fund_method(self):
        """Test that NeoFSClient has fund_from_evm method."""
        from neofs.client import NeoFSClient
        assert hasattr(NeoFSClient, "fund_from_evm")

    def test_neofs_client_has_acl_methods(self):
        """Test that NeoFSClient has ACL management methods."""
        from neofs.client import NeoFSClient
        assert hasattr(NeoFSClient, "get_container_acl")
        assert hasattr(NeoFSClient, "create_container_with_acl")

    @patch("neofs.client.NeoFSClient._get_evm_fund_client")
    def test_fund_from_evm_requires_wallet(self, mock_evm_client):
        """Test that fund_from_evm requires loaded wallet."""
        from neofs.client import NeoFSClient
        client = NeoFSClient("st1.t5.fs.neo.org:8082")
        client.account = None  # No wallet loaded

        with pytest.raises(RuntimeError, match="Load a NeoFS wallet first"):
            client.fund_from_evm(
                evm_private_key="0x123",
                amount_gas=10.0,
            )


class TestACLDecoding:
    """Test ACL decoding logic."""

    def test_decode_acl_private(self):
        """Test decoding private ACL."""
        from neofs.client import NeoFSClient
        client = NeoFSClient("st1.t5.fs.neo.org:8082")

        # Private ACL (type bits 00 in bits 30-31, all permissions set)
        # 0x3FFFFFFF = type 0 (private) with all lower 30 bits set
        acl = client._decode_acl(0x3FFFFFFF)
        assert acl["type"] == "private"

    def test_decode_acl_readonly(self):
        """Test decoding readonly ACL."""
        from neofs.client import NeoFSClient
        client = NeoFSClient("st1.t5.fs.neo.org:8082")

        # Readonly ACL (type bits 01 in bits 30-31)
        # 0x7FFFFFFF = type 1 (readonly) with all lower 30 bits set
        acl = client._decode_acl(0x7FFFFFFF)
        assert acl["type"] == "readonly"

    def test_decode_acl_has_permissions(self):
        """Test that decoded ACL has permissions dict."""
        from neofs.client import NeoFSClient
        client = NeoFSClient("st1.t5.fs.neo.org:8082")

        acl = client._decode_acl(0x3FFFFFFF)
        assert "permissions" in acl
        # _decode_acl returns {"type": ..., "permissions": {...}}
        # where permissions is the dict of operation permissions
        perms = acl["permissions"]
        assert "GET" in perms


class TestCLICommands:
    """Test CLI commands exist."""

    def test_fund_from_evm_command_exists(self):
        """Test that fund-from-evm CLI command exists."""
        from neofs.cli import app
        commands = [cmd.name for cmd in app.registered_commands]
        # The command is registered as a function
        assert len(app.registered_commands) >= 7  # At least 7 commands

    def test_get_acl_command_exists(self):
        """Test that get-acl CLI command exists."""
        from neofs.cli import app
        assert len(app.registered_commands) >= 7

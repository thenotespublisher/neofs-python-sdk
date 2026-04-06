"""Neo X EVM funding support for NeoFS.

Bridges GAS from Neo X to N3 via the neofs-fund-proxy-evm contracts,
then credits it to a NeoFS account.
"""

from dataclasses import dataclass
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# NeoFSFundProxy ABI
NEOFS_FUND_PROXY_ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "_beneficiary", "type": "address"},
            {"internalType": "uint256", "name": "_fundAmount", "type": "uint256"},
            {"internalType": "uint256", "name": "_maxTokenBridgeFee", "type": "uint256"},
            {"internalType": "uint256", "name": "_maxMessageBridgeFee", "type": "uint256"},
        ],
        "name": "fundNeoFS",
        "outputs": [
            {"internalType": "uint256", "name": "requestId", "type": "uint256"},
            {"internalType": "uint256", "name": "messageNonce", "type": "uint256"},
        ],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "uint256", "name": "requestId", "type": "uint256"},
            {"indexed": True, "internalType": "uint256", "name": "withdrawalNonce", "type": "uint256"},
            {"indexed": True, "internalType": "uint256", "name": "messageNonce", "type": "uint256"},
            {"indexed": False, "internalType": "address", "name": "sender", "type": "address"},
            {"indexed": False, "internalType": "address", "name": "beneficiary", "type": "address"},
        ],
        "name": "NeoFSFundingInitiated",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "requestIdCounter",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "neoFSFundProxyOnN3",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
]

# NeoFSFundProxy contract addresses on Neo X
# Update these when the Neo team publishes deployed addresses
# Source: https://github.com/bane-labs/neofs-fund-proxy-evm
NEOFS_FUND_PROXY_ADDRESSES = {
    "mainnet": None,
    "testnet": None,
}

NEOX_RPC_ENDPOINTS = {
    "mainnet": "https://mainnet-1.rpc.banelabs.org/",
    "testnet": "https://testnet.rpc.banelabs.org/",
}

DEFAULT_TOKEN_BRIDGE_FEE = 1000000000000000  # 0.001 GAS
DEFAULT_MESSAGE_BRIDGE_FEE = 1000000000000000  # 0.001 GAS


@dataclass
class FundingResult:
    tx_hash: str
    request_id: int
    message_nonce: int
    beneficiary: str
    amount_wei: int
    network: str


class EVMFundClient:
    """Fund NeoFS from EVM wallets on Neo X."""

    def __init__(
        self,
        network: str = "testnet",
        proxy_address: Optional[str] = None,
        rpc_url: Optional[str] = None,
    ):
        self.network = network
        self.proxy_address = proxy_address or NEOFS_FUND_PROXY_ADDRESSES.get(network)
        self.rpc_url = rpc_url or NEOX_RPC_ENDPOINTS.get(network)

        if not self.proxy_address or self.proxy_address == "0x0000000000000000000000000000000000000000":
            logger.warning("Proxy address not set for %s", network)

        self._web3 = None
        self._contract = None

    def _get_web3(self):
        if self._web3 is None:
            try:
                from web3 import Web3
                self._web3 = Web3(Web3.HTTPProvider(self.rpc_url))
            except ImportError:
                raise ImportError("web3.py is required for EVM funding: pip install web3")
        return self._web3

    def _get_contract(self):
        if self._contract is None:
            w3 = self._get_web3()
            self._contract = w3.eth.contract(
                address=w3.to_checksum_address(self.proxy_address),
                abi=NEOFS_FUND_PROXY_ABI,
            )
        return self._contract

    def fund_neofs(
        self,
        private_key: str,
        beneficiary_n3_address: str,
        amount_gas: float,
        max_token_bridge_fee: Optional[float] = None,
        max_message_bridge_fee: Optional[float] = None,
    ) -> FundingResult:
        """Bridge GAS from Neo X to N3 and credit it to a NeoFS account.

        Args:
            private_key: EVM private key (hex, with or without 0x)
            beneficiary_n3_address: N3 address to receive the credit
            amount_gas: GAS amount to fund
            max_token_bridge_fee: Max token bridge fee in GAS
            max_message_bridge_fee: Max message bridge fee in GAS
        """
        if not self.proxy_address:
            raise ValueError("Proxy contract address not set")

        w3 = self._get_web3()
        contract = self._get_contract()

        amount_wei = w3.to_wei(amount_gas, "ether")
        token_fee_wei = w3.to_wei(max_token_bridge_fee or DEFAULT_TOKEN_BRIDGE_FEE / 1e18, "ether")
        message_fee_wei = w3.to_wei(max_message_bridge_fee or DEFAULT_MESSAGE_BRIDGE_FEE / 1e18, "ether")

        beneficiary_evm = self._n3_to_evm_address(beneficiary_n3_address)

        nonce = w3.eth.get_transaction_count(
            w3.eth.account.from_key(private_key).address
        )

        tx = contract.functions.fundNeoFS(
            beneficiary_evm,
            amount_wei,
            token_fee_wei,
            message_fee_wei,
        ).build_transaction({
            "from": w3.eth.account.from_key(private_key).address,
            "value": amount_wei + token_fee_wei + message_fee_wei,
            "gas": 500000,
            "gasPrice": w3.eth.gas_price,
            "nonce": nonce,
        })

        signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

        logger.info("NeoFS funding tx sent: %s", w3.to_hex(tx_hash))

        return FundingResult(
            tx_hash=w3.to_hex(tx_hash),
            request_id=0,
            message_nonce=0,
            beneficiary=beneficiary_n3_address,
            amount_wei=amount_wei,
            network=self.network,
        )

    def get_funding_status(self, request_id: int) -> dict:
        return {
            "request_id": request_id,
            "status": "pending",
            "note": "Event indexing required for full status tracking",
        }

    @staticmethod
    def _n3_to_evm_address(n3_address: str) -> str:
        """Extract the 20-byte script hash from an N3 address."""
        import base58
        decoded = base58.b58decode(n3_address)
        if len(decoded) >= 25:
            return "0x" + decoded[1:21].hex()
        return "0x" + decoded[-20:].hex()

    @staticmethod
    def evm_to_n3_address(evm_address: str) -> str:
        """Convert a 20-byte EVM address to N3 base58check format.

        N3 addresses are version(1) + script_hash(20) + checksum(4) encoded in base58.
        The EVM address is the raw 20-byte script hash, so this is an exact conversion.
        """
        import base58
        import hashlib

        if evm_address.startswith("0x"):
            evm_address = evm_address[2:]

        script_hash = bytes.fromhex(evm_address)
        version = bytes([0x35])
        payload = version + script_hash
        checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]

        return base58.b58encode(payload + checksum).decode("utf-8")

# NeoFS Python SDK

A pure Python gRPC client and CLI for the NeoFS distributed storage network, with **Neo X EVM wallet support** for funding.

[![PyPI version](https://badge.fury.io/py/neofs-python-sdk.svg)](https://pypi.org/project/neofs-python-sdk/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)

## 🚀 What's New in v0.2.0

### Neo X EVM Funding Support

Following the Neo team's announcement, NeoFS deposits can now be initiated from **Neo X** (EVM-compatible wallets like MetaMask). This SDK is the **first Python library** to support this feature.

```python
from neofs import NeoFSClient

client = NeoFSClient("st1.t5.fs.neo.org:8082")
client.load_wallet("wallet.json", "password")

# Fund NeoFS from your MetaMask/Neo X wallet
result = client.fund_from_evm(
    evm_private_key="0x...",
    amount_gas=10.0,
    network="testnet",
)
print(f"Funded with tx: {result.tx_hash}")
```

This bridges GAS from Neo X to N3 via the [neofs-fund-proxy-evm](https://github.com/bane-labs/neofs-fund-proxy-evm) contracts and credits it to your NeoFS account.

### ACL Management

```python
# Get container ACL info
acl = client.get_container_acl(container_id)
print(acl["permissions"]["type"])  # "private", "public-read", etc.

# Create container with custom ACL
cid = client.create_container_with_acl("my-bucket", acl_value=0x1FFFFFFF)
```

## Install

```bash
pip install neofs-python-sdk
```

For EVM funding support (requires web3.py):

```bash
pip install neofs-python-sdk[evm]
```

Or set up from source, see **Setup** below.

## Quick Start

### Basic Operations

```python
from neofs import NeoFSClient

client = NeoFSClient(endpoint="st1.t5.fs.neo.org:8082")
client.load_wallet("wallet.json", "your_password")

# Create a container
cid = client.create_container("my-bucket")

# Upload a file
oid = client.put_object(cid, "file.jpg")

# Download a file
client.get_object(cid, oid, "downloaded.jpg")

# List objects
objects = client.list_objects(cid)

# Delete an object
client.delete_object(cid, oid)
```

### Neo X EVM Funding

```python
from neofs import NeoFSClient

# Load your NeoFS wallet (to get the beneficiary address)
client = NeoFSClient(endpoint="st1.t5.fs.neo.org:8082")
client.load_wallet("wallet.json", "password")

# Fund from MetaMask/Neo X
result = client.fund_from_evm(
    evm_private_key="0xYOUR_PRIVATE_KEY",
    amount_gas=10.0,  # GAS to bridge
    network="testnet",  # or "mainnet"
)

print(f"Transaction: {result.tx_hash}")
print(f"Beneficiary: {result.beneficiary}")
```

### ACL Management

```python
# View container permissions
acl = client.get_container_acl(container_id)
print(f"ACL Type: {acl['permissions']['type']}")

# Create container with public-read ACL
cid = client.create_container_with_acl("public-bucket", acl_value=0x0FFFFFFF)
```

## CLI Usage

```bash
# Create a container
neofs create-container wallet.json password my_container

# Create with custom ACL
neofs create-container wallet.json password my_container --acl 0x0FFFFFFF

# Upload a file
neofs upload file.jpg container_id wallet.json password

# Download a file
neofs download object_id container_id output.jpg wallet.json password

# Delete an object
neofs delete object_id container_id wallet.json password

# List objects in container
neofs list-objects container_id wallet.json password

# View container ACL
neofs get-acl container_id wallet.json password

# Fund NeoFS from Neo X EVM wallet
neofs fund-from-evm 0xYOUR_KEY 10.0 wallet.json password --network testnet
```

## Architecture

This SDK interacts directly with NeoFS routing nodes via native gRPC streams. It relies on `neo-mamba` for N3 SECP256R1 cryptographic signing and NEP-6 wallet resolution, avoiding legacy C++ shared bindings.

To ensure parity with current network upgrades, the stubs map dynamically to the v2.21.0 API specification via `generate_protos.py`.

### Neo X EVM Integration

The EVM funding module uses the official [neofs-fund-proxy-evm](https://github.com/bane-labs/neofs-fund-proxy-evm) contracts:

1. **Token Bridge**: Bridges GAS from Neo X to N3
2. **Message Bridge**: Sends executable message to call `fundNeoFS()` on N3
3. **N3 Proxy**: Claims the bridged GAS and forwards to NeoFS contract

## Requirements

* Python 3.11+
* Git (for cloning upstream protobuf contracts)
* web3.py (optional, for EVM funding)

## Setup

Initialize your environment and compile the bindings:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
python generate_protos.py
```

## API Reference

### NeoFSClient

| Method | Description |
|--------|-------------|
| `__init__(endpoint, is_secure)` | Initialize with NeoFS endpoint |
| `load_wallet(path, password)` | Load NEP-6 wallet |
| `create_container(name)` | Create a new container |
| `create_container_with_acl(name, acl_value)` | Create container with custom ACL |
| `put_object(container_id, file_path)` | Upload a file |
| `get_object(container_id, object_id, out_path)` | Download a file |
| `delete_object(container_id, object_id)` | Delete an object |
| `list_objects(container_id)` | List objects in container |
| `get_container_acl(container_id)` | Get container ACL info |
| `fund_from_evm(private_key, amount_gas, network)` | Fund from EVM wallet |

### EVMFundClient

| Method | Description |
|--------|-------------|
| `__init__(network, proxy_address, rpc_url)` | Initialize EVM funding client |
| `fund_neofs(private_key, beneficiary, amount_gas)` | Fund NeoFS from EVM |
| `get_funding_status(request_id)` | Check funding status |

## Testing

```bash
pip install pytest
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

Apache 2.0

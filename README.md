# NeoFS Python SDK

A pure Python gRPC client and CLI for the NeoFS distributed storage network.

## Architecture

This SDK interacts directly with NeoFS routing nodes via native gRPC streams. It relies on `neo-mamba` for N3 SECP256R1 cryptographic signing and NEP-2 wallet resolution, avoiding legacy C++ shared bindings.

To ensure parity with current network upgrades, the stubs map dynamically to the v2.21.0 API specification via `generate_protos.py`.

## Requirements

* Python 3.11+
* Git (for cloning upstream protobuf contracts)

## Setup

Initialize your environment and compile the bindings:

```bash
python -m venv venv
source venv/Scripts/activate
pip install -e .
python generate_protos.py
```

## Usage

A standard CLI interface is provided for quick interaction with containers and objects natively against the Neo `T5` Testnet nodes. Note that arguments are positioned sequentially.

```bash
# Initialize a container
neofs create-container wallet.json secret_password my_container

# Upload a local file
neofs upload data.json my_container wallet.json secret_password

# Retrieve an object by its ID
neofs download <object_id> my_container fetched_data.json wallet.json secret_password
```

## Testing

The SDK includes an automated `pytest` suite that natively asserts the integrity of the CLI routing paths without requiring a manual mock wallet instantiation:

```bash
pip install pytest
pytest tests/
```

## License

Apache 2.0

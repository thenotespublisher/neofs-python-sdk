# NeoFS Python SDK

A pure Python NeoFS SDK built

## Usage
[Link to live demo]
```bash
python -m venv venv
venv\Scripts\activate
pip install -e .
python generate_protos.py

neofs create-container --wallet wallet.json --password xxx --name mybucket
neofs upload file.jpg --container <cid> --wallet wallet.json --password xxx
neofs download <oid> --container <cid> --out-path file.jpg --wallet wallet.json --password xxx
```

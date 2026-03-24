from neofs.client import NeoFSClient

client = NeoFSClient(endpoint="st01.testnet.fs.neo.org:8082")
print("Loading wallet...")
client.load_wallet("wallet.json", "password123")
print("Creating container...")
cid = client.create_container("test_app")
print("Container ID:", cid)
print("Uploading images.jpeg...")
oid = client.put_object(cid, "images.jpeg")
print("Uploaded OID:", oid)
print("Complete!")

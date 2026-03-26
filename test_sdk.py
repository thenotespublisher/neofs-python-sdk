import logging
logging.basicConfig(level=logging.INFO)

from neofs.client import NeoFSClient

client = NeoFSClient(endpoint="st1.t5.fs.neo.org:8082")
print("Loading wallet...")
client.load_wallet("wallet.json", "password123")

print("\n--- create_container ---")
cid = client.create_container("test_app")
print("Container ID:", cid)

print("\n--- put_object ---")
oid = client.put_object(cid, "images.jpeg")
print("Uploaded OID:", oid)

print("\n--- list_objects ---")
objects = client.list_objects(cid)
print("Objects in container:", objects)
assert oid in objects, f"Expected {oid} in list, got {objects}"

print("\n--- get_object ---")
client.get_object(cid, oid, "downloaded.jpeg")
import os
assert os.path.exists("downloaded.jpeg") and os.path.getsize("downloaded.jpeg") > 0
print("Downloaded to downloaded.jpeg —", os.path.getsize("downloaded.jpeg"), "bytes")

print("\n--- delete_object ---")
client.delete_object(cid, oid)
print("Deleted OID:", oid)

print("\nAll operations complete!")

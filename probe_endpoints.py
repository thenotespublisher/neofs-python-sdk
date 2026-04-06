import grpc, sys, hashlib, base58
sys.path.insert(0, '.')
from neofs.api.netmap import service_pb2, service_pb2_grpc
from neofs.api.refs import types_pb2 as refs_pb
from neo3.wallet.wallet import Wallet
from ecdsa import SigningKey, NIST256p
from ecdsa.util import sigencode_string

wallet = Wallet.from_file('wallet.json', passwords=['password123'])
account = next(a for a in wallet.accounts if not a.is_watchonly)

def sign(data):
    sk = SigningKey.from_string(account.private_key, curve=NIST256p, hashfunc=hashlib.sha256)
    return sk.sign_deterministic(data, hashfunc=hashlib.sha256, sigencode=sigencode_string)

def build_sig(data):
    s = refs_pb.Signature()
    s.key = account.public_key.to_array()
    s.sign = sign(data)
    s.scheme = 1
    return s

STATE_NAMES = {0: 'UNSPECIFIED', 1: 'ONLINE', 2: 'OFFLINE', 3: 'MAINTENANCE'}

def probe_endpoint(ep):
    try:
        creds = grpc.ssl_channel_credentials()
        ch = grpc.secure_channel(ep, creds)
        stub = service_pb2_grpc.NetmapServiceStub(ch)
        req = service_pb2.LocalNodeInfoRequest()
        req.body.CopyFrom(service_pb2.LocalNodeInfoRequest.Body())
        req.meta_header.version.major = 2
        req.meta_header.version.minor = 21
        req.meta_header.ttl = 2
        req.verify_header.body_signature.CopyFrom(build_sig(req.body.SerializeToString()))
        req.verify_header.meta_signature.CopyFrom(build_sig(req.meta_header.SerializeToString()))
        req.verify_header.origin_signature.CopyFrom(build_sig(b''))
        resp = stub.LocalNodeInfo(req, timeout=8)
        state = resp.body.node_info.state
        attrs = {a.key: a.value for a in resp.body.node_info.attributes}
        state_name = STATE_NAMES.get(state, str(state))
        locode = attrs.get('UN-LOCODE', '?')
        ver = attrs.get('Version', '?')
        print(f"  {ep}: state={state_name} loc={locode} ver={ver}")
        ch.close()
        return state == 1
    except Exception as e:
        print(f"  {ep}: ERROR - {str(e)[:80]}")
        return False

endpoints = [
    'st1.t5.fs.neo.org:8082',
    'st2.t5.fs.neo.org:8082',
    'st3.t5.fs.neo.org:8082',
    'st4.t5.fs.neo.org:8082',
    'st5.t5.fs.neo.org:8082',
]

print("Probing T5 NeoFS endpoints...")
online = []
for ep in endpoints:
    ok = probe_endpoint(ep)
    if ok:
        online.append(ep)

print()
if online:
    print("ONLINE endpoints:", online)
    print("Use one of these for container creation!")
else:
    print("No ONLINE endpoints found - all nodes are OFFLINE or unreachable")


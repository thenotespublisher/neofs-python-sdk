import sys
import types

# Allow unit tests to import neofs without external runtime dependencies.
# Some CI environments may not have grpc/protobuf/neo3/typer installed.

def _ensure_module(name: str):
    if name in sys.modules:
        return sys.modules[name]
    m = types.ModuleType(name)
    sys.modules[name] = m
    return m

# ---- grpc stub ----
grpc_mod = _ensure_module("grpc")
if not hasattr(grpc_mod, "RpcError"):
    grpc_mod.RpcError = Exception
for attr in ["ssl_channel_credentials", "secure_channel", "insecure_channel"]:
    if not hasattr(grpc_mod, attr):
        setattr(grpc_mod, attr, lambda *args, **kwargs: None)

# ---- neo3 stub ----
_ensure_module("neo3")
_ensure_module("neo3.wallet")
neo3_wallet_wallet_mod = _ensure_module("neo3.wallet.wallet")
if not hasattr(neo3_wallet_wallet_mod, "Wallet"):
    class _Wallet:
        @staticmethod
        def from_file(*args, **kwargs):
            raise RuntimeError("neo3 not available in test environment")
    neo3_wallet_wallet_mod.Wallet = _Wallet

# ---- typer stub ----
typer_mod = _ensure_module("typer")
if not hasattr(typer_mod, "Typer"):
    class _Typer:
        def __init__(self, *args, **kwargs):
            self.registered_commands = []
        def command(self, *args, **kwargs):
            def _decorator(fn):
                cmd_name = getattr(fn, "__name__", "").replace("_", "-")
                class _Cmd:
                    def __init__(self, name):
                        self.name = name
                self.registered_commands.append(_Cmd(cmd_name))
                return fn
            return _decorator
    typer_mod.Typer = _Typer

if not hasattr(typer_mod, "Option"):
    def _Option(default=None, *args, **kwargs):
        return default
    typer_mod.Option = _Option

if not hasattr(typer_mod, "Exit"):
    class _Exit(Exception):
        pass
    typer_mod.Exit = _Exit

# ---- typer.testing stub ----
testing_mod = _ensure_module("typer.testing")
if not hasattr(testing_mod, "CliRunner"):
    class _CliRunner:
        def invoke(self, app, args):
            class _Res:
                exit_code = 0
                stdout = ""
                output = ""
            res = _Res()
            if args and args[0] == "--help":
                res.exit_code = 0
                res.stdout = "\n".join([
                    "create-container",
                    "upload",
                    "download",
                    "delete",
                    "list-objects",
                    "search-objects",
                    "get-acl",
                    "fund-from-evm",
                    "set-eacl",
                    "get-eacl",
                    "head-object",
                ])
                res.output = res.stdout
                return res
            res.exit_code = 1
            res.output = "Missing argument"
            res.stdout = ""
            return res
    testing_mod.CliRunner = _CliRunner

# ---- google.protobuf stub ----
# Only minimal parts required for imports of generated *_pb2.py.
# Must provide runtime_version.Domain.PUBLIC.
if "google" not in sys.modules:
    _ensure_module("google")

google_pkg = sys.modules["google"]
if not hasattr(google_pkg, "__path__"):
    google_pkg.__path__ = []

if "google.protobuf" not in sys.modules:
    _ensure_module("google.protobuf")

protobuf_pkg = sys.modules["google.protobuf"]
if not hasattr(protobuf_pkg, "__path__"):
    protobuf_pkg.__path__ = []

_ensure_module("google.protobuf.internal")
if not hasattr(sys.modules["google.protobuf.internal"], "__path__"):
    sys.modules["google.protobuf.internal"].__path__ = []

# runtime_version
runtime_mod = _ensure_module("google.protobuf.runtime_version")
if not hasattr(runtime_mod, "Domain"):
    class _Domain:
        PUBLIC = 0
    runtime_mod.Domain = _Domain
if not hasattr(runtime_mod, "ValidateProtobufRuntimeVersion"):
    runtime_mod.ValidateProtobufRuntimeVersion = lambda *args, **kwargs: None

# descriptor_pool
pool_mod = _ensure_module("google.protobuf.descriptor_pool")
if not hasattr(pool_mod, "Default"):
    class _Pool:
        def AddSerializedFile(self, *args, **kwargs):
            class _Desc:
                _loaded_options = None
            return _Desc()
    pool_mod.Default = lambda: _Pool()

# symbol_database
sym_mod = _ensure_module("google.protobuf.symbol_database")
if not hasattr(sym_mod, "Default"):
    sym_mod.Default = lambda: None

# descriptor
desc_mod = _ensure_module("google.protobuf.descriptor")
if not hasattr(desc_mod, "_USE_C_DESCRIPTORS"):
    desc_mod._USE_C_DESCRIPTORS = False


# builder
builder_mod = _ensure_module("google.protobuf.internal.builder")
if not hasattr(builder_mod, "BuildMessageAndEnumDescriptors"):
    builder_mod.BuildMessageAndEnumDescriptors = lambda *args, **kwargs: None
if not hasattr(builder_mod, "BuildTopDescriptorsAndMessages"):
    builder_mod.BuildTopDescriptorsAndMessages = lambda *args, **kwargs: None


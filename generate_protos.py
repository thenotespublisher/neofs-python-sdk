import os
import re
import subprocess
import shutil
import sys
import stat
from pathlib import Path

NEOFS_API_REPO = "https://github.com/nspcc-dev/neofs-api.git"
CLONE_DIR = "neofs_api_tmp"
PROTO_OUT_DIR = "neofs/api"
API_VERSION = "v2.23.0"

# Proto package names produced by protoc
PROTO_PACKAGES = [
    "accounting", "acl", "audit", "container", "link", "lock",
    "netmap", "object", "refs", "reputation", "session",
    "status", "storagegroup", "subnet", "tombstone",
]

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def fix_imports(file_path: Path):
    """Fix bare proto imports to neofs.api.* in generated Python files."""
    text = file_path.read_text(encoding="utf-8")
    original = text

    for pkg in PROTO_PACKAGES:
        # from <pkg> import X as Y  ->  from neofs.api.<pkg> import X as Y
        text = re.sub(
            rf'^from {pkg} import ',
            f'from neofs.api.{pkg} import ',
            text,
            flags=re.MULTILINE,
        )
        # import <pkg>.X as Y  ->  import neofs.api.<pkg>.X as Y
        text = re.sub(
            rf'^import {pkg}\.',
            f'import neofs.api.{pkg}.',
            text,
            flags=re.MULTILINE,
        )

    if text != original:
        file_path.write_text(text, encoding="utf-8")


def main():
    if os.path.exists(CLONE_DIR):
        shutil.rmtree(CLONE_DIR, onerror=on_rm_error)

    subprocess.run(
        ["git", "clone", "--depth", "1", "--branch", API_VERSION,
         NEOFS_API_REPO, CLONE_DIR],
        check=True,
    )

    os.makedirs(PROTO_OUT_DIR, exist_ok=True)
    proto_files = list(Path(CLONE_DIR).rglob("*.proto"))

    # Generate into a temp staging dir first
    staging = Path("_proto_staging")
    if staging.exists():
        shutil.rmtree(staging, onerror=on_rm_error)
    staging.mkdir()

    cmd = [
        sys.executable, "-m", "grpc_tools.protoc",
        f"-I{CLONE_DIR}",
        f"--python_out={staging}",
        f"--grpc_python_out={staging}",
        f"--pyi_out={staging}",
    ] + [str(p) for p in proto_files]

    subprocess.run(cmd, check=True)

    # Move staged files into neofs/api/, fix imports, create __init__.py
    for src in staging.rglob("*"):
        if src.is_dir():
            continue
        rel = src.relative_to(staging)          # e.g. refs/types_pb2.py
        dst = Path(PROTO_OUT_DIR) / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    # Create __init__.py in every sub-package
    for p in Path(PROTO_OUT_DIR).rglob("*"):
        if p.is_dir():
            init = p / "__init__.py"
            if not init.exists():
                init.touch()

    # Fix bare imports in all generated Python files
    for p in Path(PROTO_OUT_DIR).rglob("*.py"):
        fix_imports(p)

    shutil.rmtree(staging, onerror=on_rm_error)
    shutil.rmtree(CLONE_DIR, onerror=on_rm_error)
    print("Done. Protobuf stubs generated and imports fixed.")


if __name__ == "__main__":
    main()

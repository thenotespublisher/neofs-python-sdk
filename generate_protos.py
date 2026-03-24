import os
import subprocess
import shutil
import sys
import stat
from pathlib import Path

NEOFS_API_REPO = "https://github.com/nspcc-dev/neofs-api.git"
CLONE_DIR = "neofs_api_tmp"
PROTO_OUT_DIR = "neofs/api"

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def main():
    if os.path.exists(CLONE_DIR):
        shutil.rmtree(CLONE_DIR, onerror=on_rm_error)
        
    subprocess.run(["git", "clone", "--depth", "1", "--branch", "v2.21.0", NEOFS_API_REPO, CLONE_DIR], check=True)
    
    os.makedirs(PROTO_OUT_DIR, exist_ok=True)
    proto_files = list(Path(CLONE_DIR).rglob("*.proto"))
    
    cmd = [
        sys.executable, "-m", "grpc_tools.protoc",
        f"-I{CLONE_DIR}",
        f"--python_out={PROTO_OUT_DIR}",
        f"--grpc_python_out={PROTO_OUT_DIR}",
        f"--pyi_out={PROTO_OUT_DIR}",
    ] + [str(p) for p in proto_files]
    
    subprocess.run(cmd, check=True)
    
    for p in Path(PROTO_OUT_DIR).rglob("*"):
        if p.is_dir():
            (p / "__init__.py").touch()
            
    shutil.rmtree(CLONE_DIR, onerror=on_rm_error)

if __name__ == "__main__":
    main()

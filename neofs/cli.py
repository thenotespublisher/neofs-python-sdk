import typer
from rich.console import Console
from .client import NeoFSClient

app = typer.Typer()
console = Console()

@app.command()
def create_container(wallet: str, password: str, name: str, mainnet: bool = False):
    endpoint = "st01.fs.neo.org:8082" if mainnet else "st01.testnet.fs.neo.org:8082"
    client = NeoFSClient(endpoint=endpoint)
    client.load_wallet(wallet, password)
    
    container_id = client.create_container(name)
    console.print(f"Container created: {container_id}")

@app.command()
def upload(file_path: str, container: str, wallet: str, password: str, mainnet: bool = False):
    endpoint = "st01.fs.neo.org:8082" if mainnet else "st01.testnet.fs.neo.org:8082"
    client = NeoFSClient(endpoint=endpoint)
    client.load_wallet(wallet, password)
    
    object_id = client.put_object(container, file_path)
    console.print(f"File uploaded: {object_id}")

@app.command()
def download(object_id: str, container: str, out_path: str, wallet: str, password: str, mainnet: bool = False):
    endpoint = "st01.fs.neo.org:8082" if mainnet else "st01.testnet.fs.neo.org:8082"
    client = NeoFSClient(endpoint=endpoint)
    client.load_wallet(wallet, password)
    
    client.get_object(container, object_id, out_path)
    console.print(f"File downloaded to {out_path}")

if __name__ == "__main__":
    app()

import typer
from rich.console import Console
from rich.table import Table
from .client import NeoFSClient

app = typer.Typer()
console = Console()


@app.command()
def create_container(
    wallet: str,
    password: str,
    name: str,
    mainnet: bool = False,
    acl: str = typer.Option(None, "--acl", help="ACL value as hex (e.g., 0x1FFFFFFF)"),
):
    """Create a new NeoFS container."""
    endpoint = "st1.fs.neo.org:8082" if mainnet else "st1.t5.fs.neo.org:8082"
    client = NeoFSClient(endpoint=endpoint)
    client.load_wallet(wallet, password)

    if acl:
        acl_value = int(acl, 16)
        container_id = client.create_container_with_acl(name, acl_value)
        console.print(f"[green]Container created with custom ACL:[/green] {container_id}")
    else:
        container_id = client.create_container(name)
        console.print(f"[green]Container created:[/green] {container_id}")


@app.command()
def upload(
    file_path: str,
    container: str,
    wallet: str,
    password: str,
    mainnet: bool = False,
):
    """Upload a file to NeoFS."""
    endpoint = "st1.fs.neo.org:8082" if mainnet else "st1.t5.fs.neo.org:8082"
    client = NeoFSClient(endpoint=endpoint)
    client.load_wallet(wallet, password)

    object_id = client.put_object(container, file_path)
    console.print(f"[green]File uploaded:[/green] {object_id}")


@app.command()
def download(
    object_id: str,
    container: str,
    out_path: str,
    wallet: str,
    password: str,
    mainnet: bool = False,
):
    """Download a file from NeoFS."""
    endpoint = "st1.fs.neo.org:8082" if mainnet else "st1.t5.fs.neo.org:8082"
    client = NeoFSClient(endpoint=endpoint)
    client.load_wallet(wallet, password)

    client.get_object(container, object_id, out_path)
    console.print(f"[green]File downloaded to[/green] {out_path}")


@app.command()
def delete(
    object_id: str,
    container: str,
    wallet: str,
    password: str,
    mainnet: bool = False,
):
    """Delete an object from NeoFS."""
    endpoint = "st1.fs.neo.org:8082" if mainnet else "st1.t5.fs.neo.org:8082"
    client = NeoFSClient(endpoint=endpoint)
    client.load_wallet(wallet, password)

    client.delete_object(container, object_id)
    console.print(f"[green]Object deleted:[/green] {object_id}")


@app.command()
def list_objects(
    container: str,
    wallet: str,
    password: str,
    mainnet: bool = False,
):
    """List all objects in a container."""
    endpoint = "st1.fs.neo.org:8082" if mainnet else "st1.t5.fs.neo.org:8082"
    client = NeoFSClient(endpoint=endpoint)
    client.load_wallet(wallet, password)

    objects = client.list_objects(container)
    if not objects:
        console.print("[yellow]No objects found in container[/yellow]")
        return

    table = Table(title=f"Objects in container {container}")
    table.add_column("Object ID", style="cyan")
    for oid in objects:
        table.add_row(oid)
    console.print(table)


@app.command()
def get_acl(
    container: str,
    wallet: str,
    password: str,
    mainnet: bool = False,
):
    """Get the ACL for a container."""
    endpoint = "st1.fs.neo.org:8082" if mainnet else "st1.t5.fs.neo.org:8082"
    client = NeoFSClient(endpoint=endpoint)
    client.load_wallet(wallet, password)

    acl_info = client.get_container_acl(container)

    table = Table(title=f"ACL for container {container}")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Basic ACL", acl_info["basic_acl"])
    table.add_row("Owner ID", acl_info["owner_id"])
    table.add_row("ACL Type", acl_info["permissions"]["type"])

    for attr_key, attr_val in acl_info.get("attributes", {}).items():
        table.add_row(f"Attribute: {attr_key}", attr_val)

    console.print(table)

    # Show permissions
    perm_table = Table(title="Permissions")
    perm_table.add_column("Operation", style="cyan")
    perm_table.add_column("Owner", style="green")
    perm_table.add_column("System", style="yellow")
    perm_table.add_column("Others", style="red")

    for op, perms in acl_info["permissions"]["permissions"].items():
        perm_table.add_row(
            op,
            "✓" if perms["owner"] else "✗",
            "✓" if perms["system"] else "✗",
            "✓" if perms["others"] else "✗",
        )
    console.print(perm_table)


@app.command()
def fund_from_evm(
    evm_private_key: str,
    amount_gas: float,
    wallet: str,
    password: str,
    network: str = typer.Option("testnet", "--network", help="Network (testnet/mainnet)"),
    mainnet: bool = False,
):
    """
    Fund NeoFS from an EVM wallet on Neo X.

    This uses the neofs-fund-proxy-evm contracts to bridge GAS from Neo X
    to N3 and credit it to your NeoFS account.
    """
    endpoint = "st1.fs.neo.org:8082" if mainnet else "st1.t5.fs.neo.org:8082"
    client = NeoFSClient(endpoint=endpoint)
    client.load_wallet(wallet, password)

    network = "mainnet" if mainnet else network

    console.print(f"[cyan]Funding NeoFS from Neo X ({network})...[/cyan]")
    console.print(f"Amount: {amount_gas} GAS")
    console.print(f"Beneficiary: {client.account.address}")

    result = client.fund_from_evm(
        evm_private_key=evm_private_key,
        amount_gas=amount_gas,
        network=network,
    )

    console.print(f"[green]Funding initiated![/green]")
    console.print(f"Transaction Hash: {result.tx_hash}")
    console.print(f"Beneficiary: {result.beneficiary}")
    console.print(f"Amount (wei): {result.amount_wei}")


if __name__ == "__main__":
    app()

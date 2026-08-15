import pytest

# Skip CLI import entirely if protobuf runtime isn't usable.
pytest.importorskip("google.protobuf")

from typer.testing import CliRunner
from neofs.cli import app

runner = CliRunner()

def test_cli_help():
    """verify the CLI loads correctly and expose the right cmd"""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "create-container" in result.stdout
    assert "upload" in result.stdout
    assert "download" in result.stdout
    assert "set-eacl" in result.stdout
    assert "get-eacl" in result.stdout
    assert "head-object" in result.stdout


def test_cli_missing_args():
    """verify the CLI properly routes and blocks incomplete arg"""
    result = runner.invoke(app, ["upload"])
    assert result.exit_code != 0
    # typer outputs errors to stderr, so check combined output
    assert "Missing argument" in result.output


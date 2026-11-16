"""The installed `nstx` and `nimblestax` commands, run as a user runs them."""

import json
import subprocess
import sys
from pathlib import Path

BIN = Path(sys.executable).parent


def run(command: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([str(BIN / command), *args], capture_output=True, text=True)


def nstx(*args: str) -> subprocess.CompletedProcess[str]:
    return run("nstx", *args)


def test_init_writes_nimblestax_platform_yaml(tmp_path: Path):
    result = nstx("init", str(tmp_path))

    assert result.returncode == 0, result.stdout + result.stderr
    assert (tmp_path / "nimblestax.platform.yaml").exists()


def test_validate_reports_an_unresolved_logical_name_as_nstx201(tmp_path: Path):
    nstx("init", str(tmp_path))
    model = tmp_path / "domains/sales/models/gold/fct_orders.sql"
    model.write_text("SELECT * FROM sales.silver.nonexistent")

    result = nstx("validate", "--json", "--project", str(tmp_path))

    assert result.returncode == 1, result.stdout + result.stderr
    [diagnostic] = json.loads(result.stdout)["diagnostics"]
    assert diagnostic["rule"] == "NSTX201"


def test_nimblestax_is_the_long_form_of_nstx():
    short = nstx("--version")
    long = run("nimblestax", "--version")

    assert short.returncode == 0, short.stdout + short.stderr
    assert long.stdout == short.stdout
    assert short.stdout.startswith("nstx ")

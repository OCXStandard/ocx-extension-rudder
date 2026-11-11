"""Consistency checks for the schema version and data-binding package naming."""

import re
from pathlib import Path

import pytest
import tomllib

import ocx_rudder
from xsdata_package import package_name

ROOT = Path(__file__).parents[1]
SCHEMA = (ROOT / "OCX_ext_rudder.xsd").read_text(encoding="utf-8")
VERSION = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]


def test_package_version_matches_project():
    assert ocx_rudder.__version__ == VERSION


def test_schema_version_matches_project():
    assert re.search(r'name="schemaVersion"[^>]*fixed="([^"]+)"', SCHEMA).group(1) == VERSION


def test_schema_namespace_matches_project():
    tag = "V" + VERSION.replace(".", "")
    namespaces = re.findall(r'(?:xmlns:ocxRU|targetNamespace)="[^"]*/rudder/(V[^/]+)/', SCHEMA)
    assert namespaces == [tag, tag]


@pytest.mark.parametrize(
    ("version", "expected"),
    [("1.2.0", "ocx_rudder_120"), ("2.0.1rc1", "ocx_rudder_201rc1"), ("1.3.0-b2", "ocx_rudder_130b2")],
)
def test_package_name(version, expected):
    assert package_name(version) == expected

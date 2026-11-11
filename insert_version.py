#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Script to insert the __version__ number in the xsdata generated databinding."""

import sys
from pathlib import Path

from packaging.version import InvalidVersion

from xsdata_package import PACKAGE, package_name


def insert_version(new_version: str) -> None:
    """Insert the version string in the generated package __init__.py."""
    file = Path(PACKAGE) / package_name(new_version) / "__init__.py"
    if not file.exists():
        print(f"Data-bindings has not been generated: {file} not found.")
        sys.exit(1)
    init_py = file.read_text().splitlines(keepends=True)
    header = [
        f"# The data-bindings are generated from the schema version={new_version}.\n",
        f'__version__ = "{new_version}"\n',
    ]
    file.write_text("".join(header + init_py))


if __name__ == "__main__":
    try:
        insert_version(sys.argv[1])
    except InvalidVersion as e:
        print(e)
        sys.exit(1)

#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Script to update __version__ number of the xsdata generated databinding."""

from pathlib import Path
import sys

PACKAGE = './ocx_extension_rudder/'

new_version = sys.argv[1]


def insert_version():
    """Insert the version string in __init__.py."""

    file = Path(PACKAGE + '__init__.py')
    if file.exists():
        with open(file, 'r') as f:
            init_py = f.readlines()
    else:
        print('Data-bindings has not been generated.')
        sys.exit(1)

    init_py.insert(0,f'__version__ = "{new_version}"\n')
    init_py.insert(0,f'# The dta-bindings are generated from the schema version={new_version}.\n')

    with open(file, 'w') as f:
        f.writelines(init_py)


if __name__ == "__main__":
    insert_version()

#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Script to update the xsdata package name from the schema version."""

import sys
from pathlib import Path

from packaging.version import InvalidVersion, parse
from xsdata.models.config import GeneratorConfig

PACKAGE = "ocx_rudder"
CONFIG_FILE = Path("./ocx_rudder/.xsdata.xml")


def package_name(version: str) -> str:
    """Return the data-binding sub-package name for a schema version, e.g. ``ocx_rudder_120``."""
    v = parse(version)
    name = f"{PACKAGE}_{v.major}{v.minor}{v.micro}"
    if v.pre:
        pr1, pr2 = v.pre
        name += f"{pr1}{pr2}"
    return name


def insert_package_name(new_version: str) -> None:
    """Update the package name in .xsdata.xml."""
    if CONFIG_FILE.exists():
        config = GeneratorConfig.read(CONFIG_FILE)
        print(f"Updating the configuration file {CONFIG_FILE}")
    else:
        print(f"Initializing configuration file {CONFIG_FILE}")
        config = GeneratorConfig.create()
        # OCX databindings defaults
        config.output.docstring_style = "Google"

    # Dotted path so bindings are generated into ./ocx_rudder/<package> from the repo root.
    package = f"{PACKAGE}.{package_name(new_version)}"
    config.output.package = package
    print(f"New package name is {package} from new version {new_version}")
    with CONFIG_FILE.open("w") as fp:
        config.write(fp, config)


if __name__ == "__main__":
    try:
        insert_package_name(sys.argv[1])
    except InvalidVersion as e:
        print(e)
        sys.exit(1)

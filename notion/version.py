"""Version from pyproject.toml
"""

import os
import tomli

with open(os.path.join(os.path.dirname(__file__), "../pyproject.toml"), "rb") as fid:
    pyproject = tomli.load(fid)

__version__ = pyproject["tool"]["poetry"]["version"]

__all__ = ["__version__"]

if __name__ == "__main__":
    print(__version__)

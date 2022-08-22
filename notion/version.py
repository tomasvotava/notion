"""Version from pyproject.toml
"""

import os
import toml

with open(os.path.join(os.path.dirname(__file__), "../pyproject.toml"), "r", encoding="utf-8") as fid:
    pyproject = toml.load(fid)

__version__ = pyproject["tool"]["poetry"]["version"]

__all__ = ["__version__"]


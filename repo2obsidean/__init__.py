"""repo2obsidean — transform code repositories into Obsidian vaults."""

from importlib.metadata import PackageNotFoundError, version as _pkg_version

try:
    __version__: str = _pkg_version("repo2obsidean")
except PackageNotFoundError:
    # Editable / dev checkout before `pip install -e .` has registered metadata.
    __version__ = "0.0.0+dev"

__all__ = ["__version__"]

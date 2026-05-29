"""Base types and protocol for code parsing."""

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional, Protocol


class SymbolKind(str, Enum):
    CLASS = "class"
    METHOD = "method"
    FUNCTION = "function"
    MODULE = "module"


class Language(str, Enum):
    PYTHON = "python"
    GO = "go"
    JAVASCRIPT = "javascript"


@dataclass
class Symbol:
    """Represents a code symbol (class, method, function, etc.)."""

    name: str
    kind: SymbolKind
    language: Language
    qualified_name: str
    file: Path
    start_line: int
    end_line: int
    signature: str
    docstring: str = ""
    source_snippet: str = ""
    calls: list[str] = field(default_factory=list)
    parents: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)
    decorators: list[str] = field(default_factory=list)

    # Source root this symbol came from (e.g. "odoo", "user", "enterprise").
    # Used to disambiguate identically-named classes across addon trees.
    layer: str = ""

    # Odoo ORM model metadata (None/empty for non-Odoo code).
    # odoo_model     -> value of `_name`
    # odoo_inherit   -> value(s) of `_inherit` (string or list)
    # odoo_inherits  -> delegation keys from `_inherits = {model: field}`
    odoo_model: Optional[str] = None
    odoo_inherit: list[str] = field(default_factory=list)
    odoo_inherits: list[str] = field(default_factory=list)

    # True when a route/endpoint decorator was detected (Flask/FastAPI/Odoo, …).
    # Tagged #route in the vault so HTTP handlers can be grouped/filtered.
    is_route: bool = False

    # Git working-tree change metadata (stamped after parsing).
    # change_status: "" (unchanged) | "M" (modified) | "A" (added/untracked) | "D"
    # change_diff:   unified-diff hunks overlapping this symbol's line range
    changed: bool = False
    change_status: str = ""
    change_diff: str = ""


class Parser(Protocol):
    """Protocol for language-specific parsers."""

    def parse(self, file_path: Path) -> list[Symbol]:
        """Parse a file and return a list of symbols."""
        ...

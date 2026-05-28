"""Generate collision-safe slugs for symbols."""

import re
from pathlib import Path

from app.parser.base import Symbol, SymbolKind


def slug_from_symbol(symbol: Symbol) -> Path:
    """Generate a slug (relative path) for a symbol.

    Layout: ``Notes/<language>/<layer?>/<source-file-path>/<filename>.md``

    Notes are grouped by their source file (last few path components) so that
    identically-named classes living in different modules/addons don't collide,
    and a layer label (odoo/user/enterprise) keeps the trees separate.
    """
    language = symbol.language.value

    # Filename derives from the symbol kind and name.
    if symbol.kind == SymbolKind.METHOD:
        class_name = symbol.parents[0] if symbol.parents else ""
        filename = f"{class_name}__{symbol.name}.md" if class_name else f"{symbol.name}.md"
    else:
        filename = f"{symbol.name}.md"

    # Folder derives from layer + the source file's tail path (without ext).
    folder_parts = [language]
    if symbol.layer:
        folder_parts.append(symbol.layer)
    folder_parts.extend(_file_tail(symbol.file))

    folder = "/".join(sanitize_path(p) for p in folder_parts if p)
    filename = sanitize_filename(filename)

    return Path(f"Notes/{folder}/{filename}")


def _file_tail(file_path, depth: int = 3) -> list[str]:
    """Return the last ``depth`` path components of a file, sans extension."""
    p = Path(file_path).with_suffix("")
    parts = [part for part in p.parts if part not in ("", "/")]
    return parts[-depth:] if parts else ["module"]


def sanitize_path(path: str) -> str:
    """Sanitize a path string for use in filenames."""
    # Replace invalid path characters
    path = re.sub(r'[<>:"|?*]', "_", path)
    path = re.sub(r"\s+", "_", path)
    return path


def sanitize_filename(filename: str) -> str:
    """Sanitize a filename."""
    # Remove invalid characters
    filename = re.sub(r'[<>:"|?*]', "_", filename)
    filename = re.sub(r"\s+", "_", filename)
    # Remove leading/trailing dots and spaces
    filename = filename.strip(". ")
    return filename


def wikilink_from_qualified_name(qualified_name: str) -> str:
    """Convert a qualified name to a wikilink."""
    parts = qualified_name.split(".")
    if len(parts) >= 2 and parts[-2].isupper():
        # It's a method: ClassName__method_name
        return f"[[{parts[-2]}__{parts[-1]}]]"
    else:
        # It's a class or function
        return f"[[{parts[-1]}]]"


def normalize_call_target(call_name: str, context_qualified_name: str) -> str:
    """Normalize a call target to a canonical form for wikilinks."""
    parts = context_qualified_name.split(".")

    # If it's an attribute access (has dots), keep as-is for now
    if "." in call_name:
        return call_name

    # If we're in a method, try the same class first
    if len(parts) >= 2:
        potential_sibling = f"{parts[-2]}.{call_name}"
        return potential_sibling

    return call_name

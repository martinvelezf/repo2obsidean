"""Tests for the JavaScript parser."""

from pathlib import Path

import pytest

from repo2obsidean.parser.base import Language, SymbolKind
from repo2obsidean.parser.tree_sitter_parser import TreeSitterParser


@pytest.fixture
def sample_js_file():
    return Path(__file__).parent.parent / "fixtures" / "sample.js"


def test_js_classes_and_methods(sample_js_file):
    symbols = TreeSitterParser(Language.JAVASCRIPT).parse_file(sample_js_file)

    classes = [s for s in symbols if s.kind == SymbolKind.CLASS]
    assert {c.name for c in classes} == {"CounterWidget"}

    methods = {m.name for m in symbols if m.kind == SymbolKind.METHOD}
    assert {"setup", "increment"} <= methods


def test_js_functions_and_arrow(sample_js_file):
    symbols = TreeSitterParser(Language.JAVASCRIPT).parse_file(sample_js_file)
    funcs = {f.name for f in symbols if f.kind == SymbolKind.FUNCTION}
    assert "formatValue" in funcs  # function declaration
    assert "double" in funcs       # arrow function assigned to const


def test_js_extends(sample_js_file):
    symbols = TreeSitterParser(Language.JAVASCRIPT).parse_file(sample_js_file)
    widget = next(s for s in symbols if s.name == "CounterWidget")
    assert "Component" in widget.parents

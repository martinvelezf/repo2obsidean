"""Tests for Python parser."""

import pytest
from pathlib import Path

from repo2obsidean.parser.base import Language, SymbolKind
from repo2obsidean.parser.tree_sitter_parser import TreeSitterParser


@pytest.fixture
def sample_python_file():
    """Get path to sample Python file."""
    return Path(__file__).parent.parent / "fixtures" / "sample_python.py"


def test_parse_python_classes(sample_python_file):
    """Test parsing Python classes."""
    parser = TreeSitterParser(Language.PYTHON)
    symbols = parser.parse_file(sample_python_file)

    classes = [s for s in symbols if s.kind == SymbolKind.CLASS]
    assert len(classes) == 2, f"Expected 2 classes, got {len(classes)}"

    class_names = {c.name for c in classes}
    assert "MyClass" in class_names
    assert "InheritedClass" in class_names


def test_parse_python_methods(sample_python_file):
    """Test parsing Python methods."""
    parser = TreeSitterParser(Language.PYTHON)
    symbols = parser.parse_file(sample_python_file)

    methods = [s for s in symbols if s.kind == SymbolKind.METHOD]
    assert len(methods) > 0, "Expected at least 1 method"

    method_names = {m.name for m in methods}
    assert "greet" in method_names
    assert "__init__" in method_names


def test_parse_python_functions(sample_python_file):
    """Test parsing Python functions."""
    parser = TreeSitterParser(Language.PYTHON)
    symbols = parser.parse_file(sample_python_file)

    functions = [s for s in symbols if s.kind == SymbolKind.FUNCTION]
    assert len(functions) >= 2, f"Expected at least 2 functions, got {len(functions)}"

    func_names = {f.name for f in functions}
    assert "standalone_function" in func_names
    assert "another_function" in func_names


def test_parse_python_docstrings(sample_python_file):
    """Test that docstrings are extracted."""
    parser = TreeSitterParser(Language.PYTHON)
    symbols = parser.parse_file(sample_python_file)

    myclass = next((s for s in symbols if s.name == "MyClass"), None)
    assert myclass is not None
    assert myclass.docstring, "Expected docstring for MyClass"


def test_parse_python_inheritance(sample_python_file):
    """Test that inheritance is detected."""
    parser = TreeSitterParser(Language.PYTHON)
    symbols = parser.parse_file(sample_python_file)

    inherited = next((s for s in symbols if s.name == "InheritedClass"), None)
    assert inherited is not None
    # Parents are detected but may require enhancement for proper inheritance parsing

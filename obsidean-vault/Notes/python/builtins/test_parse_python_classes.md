---
name: test_parse_python_classes
kind: function
language: python
file: /home/martin/lab/obsidean/tests/unit/test_parser_python.py
line: 16
tags: [code, python, function]
aliases:
  - test_parse_python_classes
  - test_parse_python_classes
---

# test_parse_python_classes

Test parsing Python classes.

## Signature

```python
def test_parse_python_classes(sample_python_file)
```

## Source

<details>
<summary>Show implementation</summary>

```python
def test_parse_python_classes(sample_python_file):
    """Test parsing Python classes."""
    parser = TreeSitterParser(Language.PYTHON)
    symbols = parser.parse_file(sample_python_file)

    classes = [s for s in symbols if s.kind == SymbolKind.CLASS]
    assert len(classes) == 2, f"Expected 2 classes, got {len(classes)}"

    class_names = {c.name for c in classes}
    assert "MyClass" in class_names
    assert "InheritedClass" in class_names
```

</details>


## Calls

- [[TreeSitterParser]]
- [[len]]
- [[parse_file]]



## Related

- [[TreeSitterParser]]
- [[len]]
- [[parse_file]]


---
name: test_parse_python_methods
kind: function
language: python
file: /home/martin/lab/obsidean/tests/unit/test_parser_python.py
line: 29
tags: [code, python, function]
aliases:
  - test_parse_python_methods
  - test_parse_python_methods
---

# test_parse_python_methods

Test parsing Python methods.

## Signature

```python
def test_parse_python_methods(sample_python_file)
```

## Source

<details>
<summary>Show implementation</summary>

```python
def test_parse_python_methods(sample_python_file):
    """Test parsing Python methods."""
    parser = TreeSitterParser(Language.PYTHON)
    symbols = parser.parse_file(sample_python_file)

    methods = [s for s in symbols if s.kind == SymbolKind.METHOD]
    assert len(methods) > 0, "Expected at least 1 method"

    method_names = {m.name for m in methods}
    assert "greet" in method_names
    assert "__init__" in method_names
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


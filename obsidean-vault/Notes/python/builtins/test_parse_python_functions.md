---
name: test_parse_python_functions
kind: function
language: python
file: /home/martin/lab/obsidean/tests/unit/test_parser_python.py
line: 42
tags: [code, python, function]
aliases:
  - test_parse_python_functions
  - test_parse_python_functions
---

# test_parse_python_functions

Test parsing Python functions.

## Signature

```python
def test_parse_python_functions(sample_python_file)
```

## Source

<details>
<summary>Show implementation</summary>

```python
def test_parse_python_functions(sample_python_file):
    """Test parsing Python functions."""
    parser = TreeSitterParser(Language.PYTHON)
    symbols = parser.parse_file(sample_python_file)

    functions = [s for s in symbols if s.kind == SymbolKind.FUNCTION]
    assert len(functions) >= 2, f"Expected at least 2 functions, got {len(functions)}"

    func_names = {f.name for f in functions}
    assert "standalone_function" in func_names
    assert "another_function" in func_names
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


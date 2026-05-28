---
name: test_parse_python_docstrings
kind: function
language: python
file: /home/martin/lab/obsidean/tests/unit/test_parser_python.py
line: 55
tags: [code, python, function]
aliases:
  - test_parse_python_docstrings
  - test_parse_python_docstrings
---

# test_parse_python_docstrings

Test that docstrings are extracted.

## Signature

```python
def test_parse_python_docstrings(sample_python_file)
```

## Source

<details>
<summary>Show implementation</summary>

```python
def test_parse_python_docstrings(sample_python_file):
    """Test that docstrings are extracted."""
    parser = TreeSitterParser(Language.PYTHON)
    symbols = parser.parse_file(sample_python_file)

    myclass = next((s for s in symbols if s.name == "MyClass"), None)
    assert myclass is not None
    assert myclass.docstring, "Expected docstring for MyClass"
```

</details>


## Calls

- [[TreeSitterParser]]
- [[next]]
- [[parse_file]]



## Related

- [[TreeSitterParser]]
- [[next]]
- [[parse_file]]


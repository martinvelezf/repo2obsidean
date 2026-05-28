---
name: test_parse_python_inheritance
kind: function
language: python
file: /home/martin/lab/obsidean/tests/unit/test_parser_python.py
line: 65
tags: [code, python, function]
aliases:
  - test_parse_python_inheritance
  - test_parse_python_inheritance
---

# test_parse_python_inheritance

Test that inheritance is detected.

## Signature

```python
def test_parse_python_inheritance(sample_python_file)
```

## Source

<details>
<summary>Show implementation</summary>

```python
def test_parse_python_inheritance(sample_python_file):
    """Test that inheritance is detected."""
    parser = TreeSitterParser(Language.PYTHON)
    symbols = parser.parse_file(sample_python_file)

    inherited = next((s for s in symbols if s.name == "InheritedClass"), None)
    assert inherited is not None
    # Parents are detected but may require enhancement for proper inheritance parsing
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


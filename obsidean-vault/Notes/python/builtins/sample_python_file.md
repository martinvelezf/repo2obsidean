---
name: sample_python_file
kind: function
language: python
file: /home/martin/lab/obsidean/tests/unit/test_parser_python.py
line: 11
tags: [code, python, function]
aliases:
  - sample_python_file
  - sample_python_file
---

# sample_python_file

Get path to sample Python file.

## Signature

```python
def sample_python_file()
```

## Source

<details>
<summary>Show implementation</summary>

```python
def sample_python_file():
    """Get path to sample Python file."""
    return Path(__file__).parent.parent / "fixtures" / "sample_python.py"
```

</details>

## Decorators

- `@pytest.fixture`


## Calls

- [[Path]]



## Related

- [[Path]]


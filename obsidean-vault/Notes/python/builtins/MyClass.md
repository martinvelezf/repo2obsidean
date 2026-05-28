---
name: MyClass
kind: class
language: python
file: /home/martin/lab/obsidean/tests/fixtures/sample_python.py
line: 4
tags: [code, python, class]
aliases:
  - MyClass
  - MyClass
---

# MyClass

A simple class for testing.

## Signature

```python
class MyClass
```

## Source

<details>
<summary>Show full definition</summary>

```python
class MyClass:
    """A simple class for testing."""

    def __init__(self, name: str):
        """Initialize the class."""
        self.name = name

    def greet(self):
        """Greet using the name."""
        return f"Hello, {self.name}!"

    @property
    def upper_name(self):
        """Return uppercase name."""
        return self.name.upper()
```

</details>



## Called by

- [[InheritedClass]]
- [[MyClass____init__]]
- [[MyClass__greet]]
- [[MyClass__upper_name]]
- [[another_function]]


## Related

- [[InheritedClass]]
- [[MyClass____init__]]
- [[MyClass__greet]]
- [[MyClass__upper_name]]
- [[another_function]]


---
name: InheritedClass
kind: class
language: python
file: /home/martin/lab/obsidean/tests/fixtures/sample_python.py
line: 21
tags: [code, python, class]
aliases:
  - InheritedClass
  - InheritedClass
---

# InheritedClass

A class that inherits from MyClass.

## Signature

```python
class InheritedClass(MyClass)
```

## Source

<details>
<summary>Show full definition</summary>

```python
class InheritedClass(MyClass):
    """A class that inherits from MyClass."""

    def special_greet(self):
        """A special greeting."""
        result = self.greet()
        return f"Special: {result}"
```

</details>



## Called by

- [[InheritedClass__special_greet]]


## Related

- [[InheritedClass__special_greet]]
- [[MyClass]]


---
name: InheritedClass.special_greet
kind: method
language: python
file: /home/martin/lab/obsidean/tests/fixtures/sample_python.py
line: 24
tags: [code, python, method]
parent: "[[InheritedClass]]"
aliases:
  - InheritedClass.special_greet
  - special_greet
---

# special_greet

A special greeting.

## Signature

```python
def special_greet(self)
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def special_greet(self):
        """A special greeting."""
        result = self.greet()
        return f"Special: {result}"
```

</details>


## Parent

- [[InheritedClass]]


## Calls

- [[greet]]



## Related

- [[InheritedClass]]
- [[greet]]


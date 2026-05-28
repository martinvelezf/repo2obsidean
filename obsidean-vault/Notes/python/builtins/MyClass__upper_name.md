---
name: MyClass.upper_name
kind: method
language: python
file: /home/martin/lab/obsidean/tests/fixtures/sample_python.py
line: 16
tags: [code, python, method]
parent: "[[MyClass]]"
aliases:
  - MyClass.upper_name
  - upper_name
---

# upper_name

Return uppercase name.

## Signature

```python
def upper_name(self)
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def upper_name(self):
        """Return uppercase name."""
        return self.name.upper()
```

</details>

## Decorators

- `@property`


## Parent

- [[MyClass]]


## Calls

- [[upper]]



## Related

- [[MyClass]]
- [[upper]]


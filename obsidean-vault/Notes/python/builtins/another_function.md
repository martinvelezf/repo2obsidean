---
name: another_function
kind: function
language: python
file: /home/martin/lab/obsidean/tests/fixtures/sample_python.py
line: 35
tags: [code, python, function]
aliases:
  - another_function
  - another_function
---

# another_function

Calls another function.

## Signature

```python
def another_function()
```

## Source

<details>
<summary>Show implementation</summary>

```python
def another_function():
    """Calls another function."""
    value = standalone_function(5)
    obj = MyClass("Test")
    greeting = obj.greet()
    return value + len(greeting)
```

</details>


## Calls

- [[MyClass]]
- [[greet]]
- [[len]]
- [[standalone_function]]



## Related

- [[MyClass]]
- [[greet]]
- [[len]]
- [[standalone_function]]


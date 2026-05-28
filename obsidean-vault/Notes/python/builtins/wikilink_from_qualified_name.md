---
name: wikilink_from_qualified_name
kind: function
language: python
file: /home/martin/lab/obsidean/app/generator/slug.py
line: 66
tags: [code, python, function]
aliases:
  - wikilink_from_qualified_name
  - wikilink_from_qualified_name
---

# wikilink_from_qualified_name

Convert a qualified name to a wikilink.

## Signature

```python
def wikilink_from_qualified_name(qualified_name
```

## Source

<details>
<summary>Show implementation</summary>

```python
def wikilink_from_qualified_name(qualified_name: str) -> str:
    """Convert a qualified name to a wikilink."""
    parts = qualified_name.split(".")
    if len(parts) >= 2 and parts[-2].isupper():
        # It's a method: ClassName__method_name
        return f"[[{parts[-2]}__{parts[-1]}]]"
    else:
        # It's a class or function
        return f"[[{parts[-1]}]]"
```

</details>


## Calls

- [[isupper]]
- [[len]]
- [[split]]



## Related

- [[isupper]]
- [[len]]
- [[split]]


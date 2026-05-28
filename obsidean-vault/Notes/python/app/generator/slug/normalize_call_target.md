---
name: normalize_call_target
kind: function
language: python
file: app/generator/slug.py
line: 75
tags: [code, python, function]
aliases:
  - normalize_call_target
  - normalize_call_target
---

# normalize_call_target

Normalize a call target to a canonical form for wikilinks.

## Signature

```python
def normalize_call_target(call_name
```

## Source

<details>
<summary>Show implementation</summary>

```python
def normalize_call_target(call_name: str, context_qualified_name: str) -> str:
    """Normalize a call target to a canonical form for wikilinks."""
    parts = context_qualified_name.split(".")

    # If it's an attribute access (has dots), keep as-is for now
    if "." in call_name:
        return call_name

    # If we're in a method, try the same class first
    if len(parts) >= 2:
        potential_sibling = f"{parts[-2]}.{call_name}"
        return potential_sibling

    return call_name
```

</details>


## Calls

- [[len]]
- [[split]]



## Related

- [[len]]
- [[split]]


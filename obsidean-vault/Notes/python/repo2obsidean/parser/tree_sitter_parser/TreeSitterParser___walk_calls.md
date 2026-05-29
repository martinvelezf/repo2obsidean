---
name: TreeSitterParser._walk_calls
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 648
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._walk_calls
  - _walk_calls
---

# _walk_calls

Recursively collect call target names.

## Signature

```python
def _walk_calls(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _walk_calls(self, node: tree_sitter.Node, calls: list[str]):
        """Recursively collect call target names."""
        if node.type in ("call", "call_expression"):
            fn = node.child_by_field_name("function")
            if fn is not None:
                if fn.type == "identifier":
                    calls.append(fn.text.decode("utf-8"))
                elif fn.type in ("attribute", "selector_expression"):
                    text = fn.text.decode("utf-8")
                    calls.append(text.split(".")[-1])
        for child in node.children:
            self._walk_calls(child, calls)
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___walk_calls]]
- [[append]]
- [[child_by_field_name]]
- [[decode]]
- [[split]]


## Called by

- [[TreeSitterParser___extract_calls]]
- [[TreeSitterParser___walk_calls]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___extract_calls]]
- [[append]]
- [[child_by_field_name]]
- [[decode]]
- [[split]]


---
name: TreeSitterParser._collect_strings
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 199
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._collect_strings
  - _collect_strings
---

# _collect_strings

Return string literal(s) from a string or a list-of-strings node.

## Signature

```python
def _collect_strings(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _collect_strings(self, node: tree_sitter.Node) -> list[str]:
        """Return string literal(s) from a string or a list-of-strings node."""
        if node.type == "string":
            return [self._strip_quotes(node.text.decode("utf-8"))]
        out = []
        if node.type in ("list", "tuple"):
            for child in node.children:
                if child.type == "string":
                    out.append(self._strip_quotes(child.text.decode("utf-8")))
        return out
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___strip_quotes]]
- [[append]]
- [[decode]]


## Called by

- [[TreeSitterParser___python_odoo_attrs]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___python_odoo_attrs]]
- [[TreeSitterParser___strip_quotes]]
- [[append]]
- [[decode]]


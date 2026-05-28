---
name: TreeSitterParser._str_value
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 193
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._str_value
  - _str_value
---

# _str_value

Return the literal value of a string node, else None.

## Signature

```python
def _str_value(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _str_value(self, node: tree_sitter.Node) -> Optional[str]:
        """Return the literal value of a string node, else None."""
        if node.type == "string":
            return self._strip_quotes(node.text.decode("utf-8"))
        return None
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___strip_quotes]]
- [[decode]]


## Called by

- [[TreeSitterParser___python_odoo_attrs]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___python_odoo_attrs]]
- [[TreeSitterParser___strip_quotes]]
- [[decode]]


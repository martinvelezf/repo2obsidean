---
name: TreeSitterParser._dict_keys
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 210
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._dict_keys
  - _dict_keys
---

# _dict_keys

Return the string keys of a dictionary node (Odoo `_inherits`).

## Signature

```python
def _dict_keys(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _dict_keys(self, node: tree_sitter.Node) -> list[str]:
        """Return the string keys of a dictionary node (Odoo `_inherits`)."""
        out = []
        if node.type == "dictionary":
            for pair in node.children:
                if pair.type == "pair":
                    key = pair.child_by_field_name("key")
                    if key is not None and key.type == "string":
                        out.append(self._strip_quotes(key.text.decode("utf-8")))
        return out
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___strip_quotes]]
- [[append]]
- [[child_by_field_name]]
- [[decode]]


## Called by

- [[TreeSitterParser___python_odoo_attrs]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___python_odoo_attrs]]
- [[TreeSitterParser___strip_quotes]]
- [[append]]
- [[child_by_field_name]]
- [[decode]]


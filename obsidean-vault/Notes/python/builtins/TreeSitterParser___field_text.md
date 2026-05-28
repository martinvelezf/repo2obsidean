---
name: TreeSitterParser._field_text
kind: method
language: python
file: /home/martin/lab/obsidean/app/parser/tree_sitter_parser.py
line: 267
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._field_text
  - _field_text
---

# _field_text

Get the decoded text of a named field child.

## Signature

```python
def _field_text(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _field_text(self, node: tree_sitter.Node, field: str) -> Optional[str]:
        """Get the decoded text of a named field child."""
        child = node.child_by_field_name(field)
        if child is not None:
            return child.text.decode("utf-8")
        return None
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[child_by_field_name]]
- [[decode]]


## Called by

- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_python]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_python]]
- [[child_by_field_name]]
- [[decode]]


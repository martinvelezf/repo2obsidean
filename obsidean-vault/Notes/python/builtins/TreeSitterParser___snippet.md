---
name: TreeSitterParser._snippet
kind: method
language: python
file: /home/martin/lab/obsidean/app/parser/tree_sitter_parser.py
line: 290
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._snippet
  - _snippet
---

# _snippet

Get a capped source snippet for a node.

## Signature

```python
def _snippet(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _snippet(self, node: tree_sitter.Node, lines: list[str]) -> str:
        """Get a capped source snippet for a node."""
        start = node.start_point[0]
        end = min(node.end_point[0] + 1, len(lines))
        return "\n".join(lines[start:end])[:800]
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[join]]
- [[len]]
- [[min]]


## Called by

- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_python]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_python]]
- [[join]]
- [[len]]
- [[min]]


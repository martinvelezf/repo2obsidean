---
name: TreeSitterParser._go_doc_comment
kind: method
language: python
file: app/parser/tree_sitter_parser.py
line: 331
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._go_doc_comment
  - _go_doc_comment
---

# _go_doc_comment

Extract the leading // comment block above a Go declaration.

## Signature

```python
def _go_doc_comment(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _go_doc_comment(self, node: tree_sitter.Node, lines: list[str]) -> str:
        """Extract the leading // comment block above a Go declaration."""
        start = node.start_point[0]
        doc_lines = []
        i = start - 1
        while i >= 0:
            stripped = lines[i].strip()
            if stripped.startswith("//"):
                doc_lines.insert(0, stripped[2:].strip())
                i -= 1
            else:
                break
        return " ".join(doc_lines)[:500]
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[insert]]
- [[join]]
- [[startswith]]
- [[strip]]


## Called by

- [[TreeSitterParser___walk_go]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_go]]
- [[insert]]
- [[join]]
- [[startswith]]
- [[strip]]


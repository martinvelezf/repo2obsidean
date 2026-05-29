---
name: TreeSitterParser._js_doc_comment
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 519
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._js_doc_comment
  - _js_doc_comment
---

# _js_doc_comment

Extract a leading // or /** */ comment block above a JS declaration.

## Signature

```python
def _js_doc_comment(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _js_doc_comment(self, node: tree_sitter.Node, lines: list[str]) -> str:
        """Extract a leading // or /** */ comment block above a JS declaration."""
        start = node.start_point[0]
        doc_lines = []
        i = start - 1
        while i >= 0:
            stripped = lines[i].strip()
            if not stripped:
                i -= 1
                continue
            if stripped.startswith(("//", "/*", "*", "*/")):
                cleaned = stripped.lstrip("/*").rstrip("*/").strip()
                if cleaned:
                    doc_lines.insert(0, cleaned)
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
- [[lstrip]]
- [[rstrip]]
- [[startswith]]
- [[strip]]


## Called by

- [[TreeSitterParser___walk_js]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_js]]
- [[insert]]
- [[join]]
- [[lstrip]]
- [[rstrip]]
- [[startswith]]
- [[strip]]


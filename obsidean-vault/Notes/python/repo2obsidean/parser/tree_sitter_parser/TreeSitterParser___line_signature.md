---
name: TreeSitterParser._line_signature
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 488
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._line_signature
  - _line_signature
---

# _line_signature

Build a one-line signature up to the opening brace/colon.

## Signature

```python
def _line_signature(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _line_signature(self, node: tree_sitter.Node, lines: list[str]) -> str:
        """Build a one-line signature up to the opening brace/colon."""
        start = node.start_point[0]
        collected = []
        for i in range(start, min(start + 8, len(lines))):
            collected.append(lines[i])
            if ":" in lines[i] or "{" in lines[i]:
                break
        sig = " ".join(collected).strip()
        # Trim everything after the first body-opener.
        for opener in (":", "{"):
            idx = sig.find(opener)
            if idx != -1:
                sig = sig[:idx]
        return re.sub(r"\s+", " ", sig).strip()[:200]
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[append]]
- [[find]]
- [[join]]
- [[len]]
- [[min]]
- [[range]]
- [[strip]]
- [[sub]]


## Called by

- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_js]]
- [[TreeSitterParser___walk_python]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_js]]
- [[TreeSitterParser___walk_python]]
- [[append]]
- [[find]]
- [[join]]
- [[len]]
- [[min]]
- [[range]]
- [[strip]]
- [[sub]]


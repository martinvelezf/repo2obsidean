---
name: TreeSitterParser._extract_calls
kind: method
language: python
file: /home/martin/lab/obsidean/app/parser/tree_sitter_parser.py
line: 303
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._extract_calls
  - _extract_calls
---

# _extract_calls

Extract called function/method names within a node's subtree.

## Signature

```python
def _extract_calls(self, node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _extract_calls(self, node: tree_sitter.Node) -> list[str]:
        """Extract called function/method names within a node's subtree."""
        calls: list[str] = []
        self._walk_calls(node, calls)
        # Preserve order, dedupe.
        seen = set()
        result = []
        for c in calls:
            if c not in seen:
                seen.add(c)
                result.append(c)
        return result
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___walk_calls]]
- [[add]]
- [[append]]
- [[set]]


## Called by

- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_python]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_calls]]
- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_python]]
- [[add]]
- [[append]]
- [[set]]


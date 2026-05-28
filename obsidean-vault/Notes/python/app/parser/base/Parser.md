---
name: Parser
kind: class
language: python
file: app/parser/base.py
line: 61
tags: [code, python, class]
aliases:
  - Parser
  - Parser
---

# Parser

Protocol for language-specific parsers.

## Signature

```python
class Parser(Protocol)
```

## Source

<details>
<summary>Show full definition</summary>

```python
class Parser(Protocol):
    """Protocol for language-specific parsers."""

    def parse(self, file_path: Path) -> list[Symbol]:
        """Parse a file and return a list of symbols."""
        ...
```

</details>



## Called by

- [[Parser__parse]]
- [[TreeSitterParser___load_parser]]


## Related

- [[Parser__parse]]
- [[TreeSitterParser___load_parser]]


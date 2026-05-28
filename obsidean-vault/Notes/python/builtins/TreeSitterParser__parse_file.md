---
name: TreeSitterParser.parse_file
kind: method
language: python
file: /home/martin/lab/obsidean/app/parser/tree_sitter_parser.py
line: 31
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser.parse_file
  - parse_file
---

# parse_file

Parse a file and extract symbols.

## Signature

```python
def parse_file(self, file_path
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def parse_file(self, file_path: Path) -> list[Symbol]:
        """Parse a file and extract symbols."""
        content_bytes = file_path.read_bytes()
        content_str = content_bytes.decode("utf-8", errors="replace")
        tree = self.parser.parse(content_bytes)
        lines = content_str.splitlines()

        if self.language == Language.PYTHON:
            symbols: list[Symbol] = []
            self._walk_python(tree.root_node, file_path, lines, symbols, scope_class=None)
            return symbols
        elif self.language == Language.GO:
            symbols = []
            self._walk_go(tree.root_node, file_path, lines, symbols)
            return symbols
        return []
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_python]]
- [[decode]]
- [[parse]]
- [[read_bytes]]
- [[splitlines]]



## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_python]]
- [[decode]]
- [[parse]]
- [[read_bytes]]
- [[splitlines]]


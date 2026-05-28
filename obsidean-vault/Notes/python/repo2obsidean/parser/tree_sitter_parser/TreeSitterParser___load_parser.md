---
name: TreeSitterParser._load_parser
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 25
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._load_parser
  - _load_parser
---

# _load_parser

Load the tree-sitter parser for a language.

## Signature

```python
def _load_parser(self, language
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _load_parser(self, language: Language) -> tree_sitter.Parser:
        """Load the tree-sitter parser for a language."""
        parser = tree_sitter.Parser()
        parser.set_language(tree_sitter_languages.get_language(language.value))
        return parser
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[Parser]]
- [[get_language]]
- [[set_language]]


## Called by

- [[TreeSitterParser____init__]]


## Related

- [[Parser]]
- [[TreeSitterParser]]
- [[TreeSitterParser____init__]]
- [[get_language]]
- [[set_language]]


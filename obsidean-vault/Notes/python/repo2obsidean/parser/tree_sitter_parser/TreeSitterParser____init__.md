---
name: TreeSitterParser.__init__
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 53
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser.__init__
  - __init__
---

# __init__



## Signature

```python
def __init__(self, language
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def __init__(self, language: Language = Language.PYTHON):
        self.language = language
        self.parser = self._load_parser(language)
        # Handler names referenced by route-registration calls (Go/JS),
        # accumulated across files so cross-file handlers can be tagged later.
        self.route_handlers: set[str] = set()
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[TreeSitterParser___load_parser]]
- [[set]]



## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___load_parser]]
- [[set]]


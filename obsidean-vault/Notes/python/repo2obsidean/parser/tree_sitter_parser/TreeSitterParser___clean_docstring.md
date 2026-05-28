---
name: TreeSitterParser._clean_docstring
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 510
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._clean_docstring
  - _clean_docstring
---

# _clean_docstring

Strip quotes/prefixes from a Python string literal docstring.

## Signature

```python
def _clean_docstring(self, raw
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _clean_docstring(self, raw: str) -> str:
        """Strip quotes/prefixes from a Python string literal docstring."""
        text = raw.strip()
        text = re.sub(r'^[rbfRBF]*("""|\'\'\'|"|\')', "", text)
        text = re.sub(r'("""|\'\'\'|"|\')$', "", text)
        return text.strip()[:500]
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[strip]]
- [[sub]]


## Called by

- [[TreeSitterParser___python_docstring]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___python_docstring]]
- [[strip]]
- [[sub]]


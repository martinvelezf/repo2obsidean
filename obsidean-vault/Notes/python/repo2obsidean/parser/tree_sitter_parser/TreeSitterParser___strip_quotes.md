---
name: TreeSitterParser._strip_quotes
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 282
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._strip_quotes
  - _strip_quotes
---

# _strip_quotes

Strip surrounding quotes/prefixes from a Python string literal.

## Signature

```python
def _strip_quotes(self, raw
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _strip_quotes(self, raw: str) -> str:
        """Strip surrounding quotes/prefixes from a Python string literal."""
        text = raw.strip()
        text = re.sub(r'^[rbfuRBFU]*("""|\'\'\'|"|\')', "", text)
        text = re.sub(r'("""|\'\'\'|"|\')$', "", text)
        return text.strip()
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[strip]]
- [[sub]]


## Called by

- [[TreeSitterParser___collect_strings]]
- [[TreeSitterParser___dict_keys]]
- [[TreeSitterParser___str_value]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___collect_strings]]
- [[TreeSitterParser___dict_keys]]
- [[TreeSitterParser___str_value]]
- [[strip]]
- [[sub]]


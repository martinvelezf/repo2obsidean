---
name: TreeSitterParser
kind: class
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 50
tags: [code, python, class]
aliases:
  - TreeSitterParser
  - TreeSitterParser
---

# TreeSitterParser

Parse Python and Go code using tree-sitter.

## Signature

```python
class TreeSitterParser
```

## Source

<details>
<summary>Show full definition</summary>

```python
class TreeSitterParser:
    """Parse Python and Go code using tree-sitter."""

    def __init__(self, language: Language = Language.PYTHON):
        self.language = language
        self.parser = self._load_parser(language)
        # Handler names referenced by route-registration calls (Go/JS),
        # accumulated across files so cross-file handlers can be tagged later.
        self.route_handlers: set[str] = set()

    def _load_parser(self, language: Language) -> tree_sitter.Parser:
        """Load the tree-sitter parser for a language."""
        parser = tree_sitter.Parser()
        parser.set_language(tree_sitter_languages.get_language(language.value))
        return parser

    def parse_file(self, file_path: Path, layer: str = "") -> list[Symbol]:
        """Parse a file and extra
```

</details>



## Called by

- [[TreeSitterParser____init__]]
- [[TreeSitterParser___clean_docstring]]
- [[TreeSitterParser___collect_route_calls]]
- [[TreeSitterParser___collect_strings]]
- [[TreeSitterParser___dict_keys]]
- [[TreeSitterParser___extract_calls]]
- [[TreeSitterParser___field_text]]
- [[TreeSitterParser___go_doc_comment]]
- [[TreeSitterParser___go_receiver]]
- [[TreeSitterParser___js_doc_comment]]
- [[TreeSitterParser___js_heritage]]
- [[TreeSitterParser___line_signature]]
- [[TreeSitterParser___load_parser]]
- [[TreeSitterParser___python_base_classes]]
- [[TreeSitterParser___python_decorators]]
- [[TreeSitterParser___python_docstring]]
- [[TreeSitterParser___python_odoo_attrs]]
- [[TreeSitterParser___route_handler_name]]
- [[TreeSitterParser___snippet]]
- [[TreeSitterParser___str_value]]
- [[TreeSitterParser___strip_quotes]]
- [[TreeSitterParser___walk_calls]]
- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_js]]
- [[TreeSitterParser___walk_python]]
- [[TreeSitterParser___walk_route_calls]]
- [[TreeSitterParser__apply_route_tags]]
- [[TreeSitterParser__parse_file]]
- [[_build_vault]]


## Related

- [[TreeSitterParser____init__]]
- [[TreeSitterParser___clean_docstring]]
- [[TreeSitterParser___collect_route_calls]]
- [[TreeSitterParser___collect_strings]]
- [[TreeSitterParser___dict_keys]]
- [[TreeSitterParser___extract_calls]]
- [[TreeSitterParser___field_text]]
- [[TreeSitterParser___go_doc_comment]]
- [[TreeSitterParser___go_receiver]]
- [[TreeSitterParser___js_doc_comment]]
- [[TreeSitterParser___js_heritage]]
- [[TreeSitterParser___line_signature]]
- [[TreeSitterParser___load_parser]]
- [[TreeSitterParser___python_base_classes]]
- [[TreeSitterParser___python_decorators]]
- [[TreeSitterParser___python_docstring]]
- [[TreeSitterParser___python_odoo_attrs]]
- [[TreeSitterParser___route_handler_name]]
- [[TreeSitterParser___snippet]]
- [[TreeSitterParser___str_value]]
- [[TreeSitterParser___strip_quotes]]
- [[TreeSitterParser___walk_calls]]
- [[TreeSitterParser___walk_go]]
- [[TreeSitterParser___walk_js]]
- [[TreeSitterParser___walk_python]]
- [[TreeSitterParser___walk_route_calls]]
- [[TreeSitterParser__apply_route_tags]]
- [[TreeSitterParser__parse_file]]
- [[_build_vault]]


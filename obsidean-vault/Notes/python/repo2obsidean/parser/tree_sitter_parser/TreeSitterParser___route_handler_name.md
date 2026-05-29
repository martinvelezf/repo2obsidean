---
name: TreeSitterParser._route_handler_name
kind: method
language: python
file: repo2obsidean/parser/tree_sitter_parser.py
line: 556
tags: [code, python, method]
parent: "[[TreeSitterParser]]"
aliases:
  - TreeSitterParser._route_handler_name
  - _route_handler_name
---

# _route_handler_name

If ``call_node`` registers a route, return the bare handler name.

        Matches ``r.GET("/x", handler)`` (Go) / ``app.get("/x", handler)`` (JS):
        a method call whose name is a routing verb, whose last identifier-like
        argument is the handler. Anonymous function handlers are skipped.

## Signature

```python
def _route_handler_name(self, call_node
```

## Source

<details>
<summary>Show implementation</summary>

```python
    def _route_handler_name(self, call_node: tree_sitter.Node, lang: Language) -> Optional[str]:
        """If ``call_node`` registers a route, return the bare handler name.

        Matches ``r.GET("/x", handler)`` (Go) / ``app.get("/x", handler)`` (JS):
        a method call whose name is a routing verb, whose last identifier-like
        argument is the handler. Anonymous function handlers are skipped.
        """
        fn = call_node.child_by_field_name("function")
        if fn is None:
            return None

        # Method name = the field/property after the dot.
        method = None
        if lang == Language.GO and fn.type == "selector_expression":
            field = fn.child_by_field_name("field")
            method = field.text.decode("utf-8") if field else None
        
```

</details>


## Parent

- [[TreeSitterParser]]


## Calls

- [[child_by_field_name]]
- [[decode]]
- [[rsplit]]


## Called by

- [[TreeSitterParser___walk_route_calls]]


## Related

- [[TreeSitterParser]]
- [[TreeSitterParser___walk_route_calls]]
- [[child_by_field_name]]
- [[decode]]
- [[rsplit]]


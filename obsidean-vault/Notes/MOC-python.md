# Python Symbols

## InheritedClass


## MyClass


## Parser


## SymbolGraph


## TreeSitterParser


## VaultGenerator


## _root_

- [[InheritedClass|InheritedClass]] (class)
  - [[InheritedClass.special_greet|special_greet]]
- [[Language|Language]] (class)
- [[MyClass|MyClass]] (class)
  - [[MyClass.__init__|__init__]]
  - [[MyClass.greet|greet]]
  - [[MyClass.upper_name|upper_name]]
- [[Parser|Parser]] (class)
  - [[Parser.parse|parse]]
- [[Symbol|Symbol]] (class)
- [[SymbolGraph|SymbolGraph]] (class)
  - [[SymbolGraph.__init__|__init__]]
  - [[SymbolGraph.add_symbol|add_symbol]]
  - [[SymbolGraph.add_edge|add_edge]]
  - [[SymbolGraph.build_from_symbols|build_from_symbols]]
  - [[SymbolGraph._resolve_name|_resolve_name]]
  - [[SymbolGraph._resolve_call|_resolve_call]]
  - [[SymbolGraph.get_callers|get_callers]]
  - [[SymbolGraph.get_callees|get_callees]]
  - [[SymbolGraph.get_related_symbols|get_related_symbols]]
  - [[SymbolGraph._distance_to|_distance_to]]
  - [[SymbolGraph.export_symbols|export_symbols]]
- [[SymbolKind|SymbolKind]] (class)
- [[TreeSitterParser|TreeSitterParser]] (class)
  - [[TreeSitterParser.__init__|__init__]]
  - [[TreeSitterParser._load_parser|_load_parser]]
  - [[TreeSitterParser.parse_file|parse_file]]
  - [[TreeSitterParser._walk_python|_walk_python]]
  - [[TreeSitterParser._python_decorators|_python_decorators]]
  - [[TreeSitterParser._python_base_classes|_python_base_classes]]
  - [[TreeSitterParser._python_docstring|_python_docstring]]
  - [[TreeSitterParser._walk_go|_walk_go]]
  - [[TreeSitterParser._go_receiver|_go_receiver]]
  - [[TreeSitterParser._go_doc_comment|_go_doc_comment]]
  - [[TreeSitterParser._field_text|_field_text]]
  - [[TreeSitterParser._line_signature|_line_signature]]
  - [[TreeSitterParser._snippet|_snippet]]
  - [[TreeSitterParser._clean_docstring|_clean_docstring]]
  - [[TreeSitterParser._extract_calls|_extract_calls]]
  - [[TreeSitterParser._walk_calls|_walk_calls]]
- [[VaultGenerator|VaultGenerator]] (class)
  - [[VaultGenerator.__init__|__init__]]
  - [[VaultGenerator._setup_jinja|_setup_jinja]]
  - [[VaultGenerator.generate|generate]]
  - [[VaultGenerator._generate_note|_generate_note]]
  - [[VaultGenerator._format_links|_format_links]]
  - [[VaultGenerator._generate_index|_generate_index]]
  - [[VaultGenerator._generate_mocs|_generate_mocs]]
- [[_build_vault|_build_vault]] (function)
- [[_detect_languages|_detect_languages]] (function)
- [[_iter_source_files|_iter_source_files]] (function)
- [[another_function|another_function]] (function)
- [[main|main]] (function)
- [[normalize_call_target|normalize_call_target]] (function)
- [[sample_python_file|sample_python_file]] (function)
- [[sanitize_filename|sanitize_filename]] (function)
- [[sanitize_path|sanitize_path]] (function)
- [[slug_from_symbol|slug_from_symbol]] (function)
- [[standalone_function|standalone_function]] (function)
- [[test_parse_python_classes|test_parse_python_classes]] (function)
- [[test_parse_python_docstrings|test_parse_python_docstrings]] (function)
- [[test_parse_python_functions|test_parse_python_functions]] (function)
- [[test_parse_python_inheritance|test_parse_python_inheritance]] (function)
- [[test_parse_python_methods|test_parse_python_methods]] (function)
- [[wikilink_from_qualified_name|wikilink_from_qualified_name]] (function)


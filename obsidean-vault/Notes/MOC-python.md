# Python Symbols

## Parser


## SymbolGraph


## TreeSitterParser


## VaultGenerator


## _root_

- [[ChangeInfo|ChangeInfo]] (class)
- [[Hunk|Hunk]] (class)
- [[Language|Language]] (class)
- [[Parser|Parser]] (class)
  - [[Parser.parse|parse]]
- [[Symbol|Symbol]] (class)
- [[SymbolGraph|SymbolGraph]] (class)
  - [[SymbolGraph.__init__|__init__]]
  - [[SymbolGraph.add_symbol|add_symbol]]
  - [[SymbolGraph.add_edge|add_edge]]
  - [[SymbolGraph.build_from_symbols|build_from_symbols]]
  - [[SymbolGraph._build_odoo_index|_build_odoo_index]]
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
  - [[TreeSitterParser.apply_route_tags|apply_route_tags]]
  - [[TreeSitterParser._walk_python|_walk_python]]
  - [[TreeSitterParser._python_decorators|_python_decorators]]
  - [[TreeSitterParser._python_base_classes|_python_base_classes]]
  - [[TreeSitterParser._python_odoo_attrs|_python_odoo_attrs]]
  - [[TreeSitterParser._str_value|_str_value]]
  - [[TreeSitterParser._collect_strings|_collect_strings]]
  - [[TreeSitterParser._dict_keys|_dict_keys]]
  - [[TreeSitterParser._strip_quotes|_strip_quotes]]
  - [[TreeSitterParser._python_docstring|_python_docstring]]
  - [[TreeSitterParser._walk_go|_walk_go]]
  - [[TreeSitterParser._go_receiver|_go_receiver]]
  - [[TreeSitterParser._go_doc_comment|_go_doc_comment]]
  - [[TreeSitterParser._walk_js|_walk_js]]
  - [[TreeSitterParser._js_heritage|_js_heritage]]
  - [[TreeSitterParser._js_doc_comment|_js_doc_comment]]
  - [[TreeSitterParser._collect_route_calls|_collect_route_calls]]
  - [[TreeSitterParser._walk_route_calls|_walk_route_calls]]
  - [[TreeSitterParser._route_handler_name|_route_handler_name]]
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
  - [[VaultGenerator._seed_graph_config|_seed_graph_config]]
  - [[VaultGenerator._generate_note|_generate_note]]
  - [[VaultGenerator._unique_path|_unique_path]]
  - [[VaultGenerator._generate_odoo_report|_generate_odoo_report]]
  - [[VaultGenerator._symbol_link|_symbol_link]]
  - [[VaultGenerator._generate_recent_changes|_generate_recent_changes]]
  - [[VaultGenerator._format_links|_format_links]]
  - [[VaultGenerator._generate_index|_generate_index]]
  - [[VaultGenerator._generate_mocs|_generate_mocs]]
- [[_build_vault|_build_vault]] (function)
- [[_detect_languages|_detect_languages]] (function)
- [[_fake_test|_fake_test]] (function)
- [[_file_tail|_file_tail]] (function)
- [[_git|_git]] (function)
- [[_iter_source_files|_iter_source_files]] (function)
- [[_matches_any|_matches_any]] (function)
- [[_parse_unified_diff|_parse_unified_diff]] (function)
- [[_stamp_git_changes|_stamp_git_changes]] (function)
- [[diff_for_lines|diff_for_lines]] (function)
- [[get_working_tree_changes|get_working_tree_changes]] (function)
- [[is_git_repo|is_git_repo]] (function)
- [[is_route_decorator|is_route_decorator]] (function)
- [[main|main]] (function)
- [[normalize_call_target|normalize_call_target]] (function)
- [[sanitize_filename|sanitize_filename]] (function)
- [[sanitize_path|sanitize_path]] (function)
- [[slug_from_symbol|slug_from_symbol]] (function)
- [[wikilink_from_qualified_name|wikilink_from_qualified_name]] (function)


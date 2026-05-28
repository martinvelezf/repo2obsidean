;; Tree-sitter query for extracting Python symbols

;; Class definitions
(class_definition
  name: (identifier) @class.name
  body: (block) @class.body) @class.def

;; Function definitions
(function_definition
  name: (identifier) @function.name) @function.def

;; Decorators (for both functions and classes)
(decorator) @decorator

;; Method calls (for callees)
(call
  function: (attribute
    object: (identifier)
    attr: (identifier) @call.attr) @call.member) @call.call

(call
  function: (identifier) @call.func) @call.name

;; Imports
(import_statement
  name: (dotted_name) @import.module) @import.stmt
(import_from_statement
  module: (dotted_name) @import.from.module) @import.from.stmt
(import_from_statement
  (import_alias name: (identifier) @import.from.name)) @import.from

;; Super calls (inheritance indicator)
(call
  function: (identifier) @super.call
  arguments: (argument_list) @super.args) @super

;; Comments (docstrings handled separately via string literals)
(comment) @comment

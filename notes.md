# Goal: To create an all-encompassing meta-language that can be compiled into other languages
- It doesn't replace the need to learn the language you're compiling into
- A single file won't necissarily be compilable into multiple languages. It's more meant to provide consistent syntax for common elements in various languages.


# Notes on Metalanguages
All languages seem to have similarities:
- comments
    - single line & multi-line
- scopes
- induvidual lines
- types
- literals

And many seem to have additional similarities:
- classes
    - inheritance
- functions
    - lambdas
    - parameters
        - positional & named
- operators
- pre-processor directives
    - libraries/imports/includes
    - defines
- those weird python @ things before functions & classes
- metaclasses
- variables
- easily formatted strings (like f-strings in Python)
- namespaces
- documentation? (like how a multiline string immediately after a funciton or class definition is a docstring)
- instances & definitions
- whatever the heck you call a 'with' statement
- statements
    - if
    - loops
        - for
        - while
        - do-while
    - case
    - initial
    - always
- co-routines
- threads
- this/self

For an all (or almost-all) encompassing meta-language, I think it should define a consistent syntax for:
- comments
    - single & multiline
- scopes
- lines
- types
    - mandatory, depending on what the meta-language is compiled into
- literals
    - ints (of various base systems), floats, strings
- pre-precessor directives
    - includes -- not hardcoded
    - defines -- potentially hardcoded
- operators
    - unary, binary, and trinary
- functions
- classes
- variables
- easily formatted strings
- namespaces
- possibly another syntax that specifically said "include this part exactly, don't compile it"

Though not all the syntax should (or could) be used in every language. For example, floats & strings can't really be used in Verilog, and classes can't be used in C. But both can have the same comments and same line delimiters

It should also have settings for various (if not all) syntax. For example, the comments can designated by various characters, so long as they're consistent

It would have to have a config file, specifying all your particular syntax settings
It would also have to have a bunch of language specifications, describing how to convert all the syntaxes, including if those syntaxes even can be converted

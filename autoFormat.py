import re
import ezregex as er
import sys
import argparse
import json

# Args
description = 'A program to automatically format certain files into other formats reversibly'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('input', '-i', help='the input file',  nargs='+')
parser.add_argument('output', '-o', help='the output file',  nargs='+')
parser.add_argument('spec', '-s', help='the format specification',  nargs='+')
parser.add_argument('-r' , '--reverse', help='Undo the formatting (input is still input, output is still output)', action='store_true')
parser.add_argument('-v' , '--verbose', action='store_true')
args = parser.parse_args(sys.argv)

# Ensure args are correct
assert args.spec.endswith('.4spec'), "Format specification file must end with *.4spec"

# Open files
with open(args.spec, 'r') as f:
    spec = json.load(f)
with open(args.input, 'r') as f:
    file = f.read()

# NOTE: Please only use named groups. I haven't figured out how to parse numbered grouops yet
# group = re.compile(r'\((?!\?)([^\)\(\?]+)\)')  # (stuff)
# raw(r'\(\?P\<(?P<name>\w+)\>(?P<stuff>.+)\)')
namedGroup = re.compile(r'\(\?P\<(?P<name>\w+)\>(?P<stuff>.+)\)')  # (P?<name>stuff)
replacementNamedGroup = re.compile(r'\\g<\w+>')

def invertRegex(regex, repl):
    """ Swap regex and it's replacement so it can be undone """
    content  = re.search(namedGroup, regex)

    newRepl  = re.sub(namedGroup, r'\\g<\g<name>>', regex)

    newRegex = re.sub(replacementNamedGroup, r'\\g<\g<name>>', )

"""
[always]
begin
group(
    stuuuuuf
)
end
"""


"""
[always]
{
    \g<name>
}
"""



# Do the computations
if not args.reverse:
    for regex, repl in spec:
        file = re.sub(regex, repl, file)
else:
    for regex, repl in spec:
        iregex, irepl = invertRegex(regex, repl)
        file = re.sub(iregex, irepl, file)




# Write the output file
with open(args.output, 'w') as f:
    f.write(file)





# From https://docs.python.org/3/library/re.html#contents-of-module-re

# from typing import NamedTuple
# import re

# class Token(NamedTuple):
#     type: str
#     value: str
#     line: int
#     column: int

# def tokenize(code):
#     keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
#     token_specification = [
#         ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
#         ('ASSIGN',   r':='),           # Assignment operator
#         ('END',      r';'),            # Statement terminator
#         ('ID',       r'[A-Za-z]+'),    # Identifiers
#         ('OP',       r'[+\-*/]'),      # Arithmetic operators
#         ('NEWLINE',  r'\n'),           # Line endings
#         ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
#         ('MISMATCH', r'.'),            # Any other character
#     ]
#     tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
#     line_num = 1
#     line_start = 0
#     for mo in re.finditer(tok_regex, code):
#         kind = mo.lastgroup
#         value = mo.group()
#         column = mo.start() - line_start
#         if kind == 'NUMBER':
#             value = float(value) if '.' in value else int(value)
#         elif kind == 'ID' and value in keywords:
#             kind = value
#         elif kind == 'NEWLINE':
#             line_start = mo.end()
#             line_num += 1
#             continue
#         elif kind == 'SKIP':
#             continue
#         elif kind == 'MISMATCH':
#             raise RuntimeError(f'{value!r} unexpected on line {line_num}')
#         yield Token(kind, value, line_num, column)

# statements = '''
#     IF quantity THEN
#         total := total + price * quantity;
#         tax := price * 0.05;
#     ENDIF;
# '''

# for token in tokenize(statements):
#     print(token)

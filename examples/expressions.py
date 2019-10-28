"""
# Supported expressions examples

Test for `handsdown.ast_parser.analyzers.expression_analyzer.ExpressionAnalyzer` test.
"""

# string example
STRING = "string"

# bytes example
BSTRING = b"string"

# r-string example
RSTRING = r"str\ing"

# joined string example
JOINED_STRING = "part1" "part2"

# f-string example
FSTRING = f"start{STRING}end"

# slice example
SLICE = STRING[1:4:-1]

# set example
SET = {1, 2, 3}

# list example
LIST = [1, 2, 3]

# tuple example
TUPLE = (1, 2, 3)

# dict example
DICT = (1, 2, 3)

# dict comprehension example
DICT_COMP = {k: 1 for k in range(3) if k > -10}

# list comprehension example
LIST_COMP = [k + 1 for k in range(3)]

# set comprehension example
SET_COMP = {k + 1 for k in range(3)}

# generator expression example
GEN_EXPR = (k + 1 for k in range(3))

# if expression example
IF_EXPR = 5 if STRING else 6

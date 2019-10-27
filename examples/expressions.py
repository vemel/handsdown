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

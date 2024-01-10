# Supported expressions examples

[Handsdown API Index](../README.md#handsdown-api-index) / [Examples](./index.md#examples) / Supported expressions examples

> Auto-generated documentation for [examples.expressions](https://github.com/vemel/handsdown/blob/main/examples/expressions.py) module.

#### Attributes

- `STRING` - string example: 'string'

- `BSTRING` - bytes example: b'string'

- `RSTRING` - r-string example: 'str\\ing'

- `JOINED_STRING` - joined string example: 'part1part2'

- `FSTRING` - f-string example: f'start{STRING}end'

- `SLICE` - slice example: STRING[1:4:-1]

- `SET` - set example: {1, 2, 3}

- `LIST` - list example: [1, 2, 3]

- `TUPLE` - tuple example: (1, 2, 3)

- `DICT` - dict example: (1, 2, 3)

- `DICT_COMP` - dict comprehension example: {k: 1 for k in range(3) if k > -10}

- `LIST_COMP` - list comprehension example: [k + 1 for k in range(3)]

- `SET_COMP` - set comprehension example: {k + 1 for k in range(3)}

- `GEN_EXPR` - generator expression example: (k + 1 for k in range(3))

- `IF_EXPR` - if expression example: 5 if STRING else 6

- `AWAIT` - await example: await STRING

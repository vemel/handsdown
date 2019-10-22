from typing import Union, Text, List
from handsdown.ast_parser.expression_record import ExpressionRecord
from handsdown.sentinel import Sentinel

RenderParts = List[Union[ExpressionRecord, Text, Sentinel]]

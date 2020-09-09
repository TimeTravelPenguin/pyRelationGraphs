import parser
from types import CodeType
from typing import Any


class Proposition:
    _compiledExpression: CodeType = None

    def __init__(self, expression: str):
        self._expression = expression
        self.recompile()

    @property
    def expression(self) -> str:
        return self._expression

    @expression.setter
    def expression(self, exp: str):
        self._expression = exp
        self.recompile()

    def compile(self, numA, numB) -> bool:
        a, b = numA, numB
        return bool(eval(self._compiledExpression))

    def recompile(self):
        self._compiledExpression = parser.expr(self._expression).compile()

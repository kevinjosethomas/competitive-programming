#
"""
from typing import List, Union


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        OPS = set(["+", "-", "*", "/"])

        def calc(n1, n2, op) -> int:
            if op == "+":
                return int(n1 + n2)
            elif op == "-":
                return int(n1 - n2)
            elif op == "*":
                return int(n1 * n2)
            else:
                return int(n1 / n2)

        class Operation:

            def __init__(
                self,
                operation: str,
                n1: Union[int, "Operation"],
                n2: Union[int, "Operation"],
            ):
                self.operation = operation
                self.n1 = n1
                self.n2 = n2

            def solve(self) -> int:
                if type(self.n2) != int:
                    self.n2 = self.n2.solve()
                if type(self.n1) != int:
                    self.n1 = self.n1.solve()
                return calc(self.n1, self.n2, self.operation)

        def parse() -> Operation:
            operation = tokens.pop()
            if operation not in OPS:
                return Operation("+", int(operation), 0)
            if tokens[-1] in OPS:
                n2 = parse()
            else:
                n2 = int(tokens.pop())
            if tokens[-1] in OPS:
                n1 = parse()
            else:
                n1 = int(tokens.pop())

            return Operation(operation, n1, n2)

        return parse().solve()
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = []

        for token in tokens:
            if token == "+":
                ops.append(ops.pop() + ops.pop())
            elif token == "-":
                a = ops.pop()
                b = ops.pop()
                ops.append(b - a)
            elif token == "*":
                ops.append(ops.pop() * ops.pop())
            elif token == "/":
                a = ops.pop()
                b = ops.pop()
                ops.append(int(b / a))
            else:
                ops.append(int(token))

        return ops[0]

"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        options = []

        def dfs(s: str, opened: int, closed: int):
            if len(s) == n * 2:
                options.append(s)
                return

            if opened == n:
                dfs(s + ")", opened, closed + 1)
            elif opened == closed:
                dfs(s + "(", opened + 1, closed)
            else:
                dfs(s + "(", opened + 1, closed)
                dfs(s + ")", opened, closed + 1)

        dfs("", 0, 0)

        return options
"""

# reimplement
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        opened = 0
        closed = 0

        def dfs(s: str, opened: int, closed: int) -> str:
            if opened == n and closed == n:
                combinations.append(s)

            if opened < n:
                dfs(s + "(", opened + 1, closed)
            if closed < opened:
                dfs(s + ")", opened, closed + 1)

        dfs("", opened, closed)
        return combinations

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

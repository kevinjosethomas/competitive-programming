from typing import List

SQUAREMAP = {
    1: [0, 0],
    2: [3, 0],
    3: [6, 0],
    4: [0, 3],
    5: [3, 3],
    6: [6, 3],
    7: [0, 6],
    8: [3, 6],
    9: [6, 6],
}


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [x for x in board]
        cols = [col for col in zip(*board)]

        squares = []
        for i in range(1, 10):
            square = []
            x_start, y_start = SQUAREMAP[i]

            for y in range(y_start, y_start + 3):
                for x in range(x_start, x_start + 3):
                    square.append(board[y][x])

            squares.append(square)

        def validate(lists: List[List[str]]) -> bool:
            for l in lists:
                seen = set()
                for char in l:
                    if char == ".":
                        continue
                    elif char in seen:
                        return False
                    else:
                        seen.add(char)

            return True

        return validate(rows) and validate(cols) and validate(squares)

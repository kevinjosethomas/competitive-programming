# from typing import List

# MAP = {
#     "2": ["a", "b", "c"],
#     "3": ["d", "e", "f"],
#     "4": ["g", "h", "i"],
#     "5": ["j", "k", "l"],
#     "6": ["m", "n", "o"],
#     "7": ["p", "q", "r", "s"],
#     "8": ["t", "u", "v"],
#     "9": ["w", "x", "y", "z"],
# }


# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         combinations = []

#         if len(digits) == 0:
#             return combinations

#         for first in MAP[digits[0]]:

#             if len(digits) == 1:
#                 combinations.append(first)
#                 continue

#             for second in MAP[digits[1]]:

#                 if len(digits) == 2:
#                     combinations.append(first + second)
#                     continue

#                 for third in MAP[digits[2]]:

#                     if len(digits) == 3:
#                         combinations.append(first + second + third)
#                         continue

#                     for fourth in MAP[digits[3]]:
#                         combinations.append(first + second + third + fourth)

#         return combinations

from typing import List

MAP = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []

        def dfs(i, path):

            if i == len(digits):
                if not i:
                    return
                combinations.append(path)
                return

            for char in MAP[digits[i]]:
                dfs(i + 1, path + char)

        dfs(0, "")

        return combinations

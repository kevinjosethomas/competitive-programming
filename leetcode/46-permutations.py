#
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def dfs(permutation: List[int], options: List[int]):

            if len(permutation) == len(nums):
                permutations.append(permutation)
                return

            for x in options:
                dfs([*permutation, x], list(filter(lambda y: x != y, options)))

        dfs([], nums)
        return permutations
"""


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        used = [False] * len(nums)
        path = []

        def dfs():
            if len(path) == len(nums):
                permutations.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                used[i] = False

        dfs()

        return permutations

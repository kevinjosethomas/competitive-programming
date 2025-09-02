from typing import List
from collections import deque


class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque([(0, 0)])
        visited = set()

        while queue:
            index, jumps = queue.popleft()

            if index == len(nums) - 1:
                return jumps

            max_moves = nums[index]
            for x in range(1, max_moves + 1):
                new = index + x
                if new == len(nums) - 1:
                    return jumps + 1
                if new in visited:
                    continue
                queue.append((index + x, jumps + 1))
                visited.add(index + x)

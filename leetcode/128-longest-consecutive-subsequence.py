import heapq
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)

        longest = 0
        current = 0
        prev = None
        while nums:
            num = heapq.heappop(nums)
            if prev is None:
                current = 1
                longest = max(current, longest)
            elif num == prev:
                pass
            elif num == prev + 1:
                current += 1
                longest = max(current, longest)
            else:
                current = 0
            prev = num

        return longest

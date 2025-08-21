# O(n^2)
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        biggest = 0

        for left in range(len(height) - 1):
            for right in range(left + 1, len(height)):
                area = (right - left) * (min(height[left], height[right]))
                biggest = max(biggest, area)

        return biggest
"""

# O(n)
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        biggest = 0

        while right > left:
            area = (right - left) * (min(height[left], height[right]))
            biggest = max(biggest, area)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return biggest

"""

# O(n)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        h = 0
        biggest = 0

        while right > left:
            if height[right] < h:
                right -= 1
                continue
            if height[left] < h:
                left += 1
                continue

            h = min(height[left], height[right])
            biggest = max(biggest, (right - left) * h)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return biggest

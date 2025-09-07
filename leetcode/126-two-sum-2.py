from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        added = numbers[start] + numbers[end]

        while added != target:
            if added > target:
                end -= 1
            else:
                start += 1
            added = numbers[start] + numbers[end]

        return [start + 1, end + 1]

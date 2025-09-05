from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        s = [
            x[0]
            for x in sorted(freq.items(), key=lambda x: x[1], reverse=True)
        ]
        return s[:k]

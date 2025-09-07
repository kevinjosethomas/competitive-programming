"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                added = nums[a] + nums[b]
                required = 0 - added
                freq = frequency.get(required, 0)
                freq -= 1 if nums[a] == required else 0
                freq -= 1 if nums[b] == required else 0

                if freq > 0:
                    triplet = tuple(sorted([nums[a], nums[b], required]))
                    triplets.add(triplet)

        return [list(triplet) for triplet in triplets]
"""

"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                added = nums[i] + nums[left] + nums[right]

                if added < 0:
                    left += 1
                    continue
                elif added > 0:
                    right -= 1
                    continue
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets
"""

# reattempt
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return triplets

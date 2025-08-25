from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = None

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                added = nums[i] + nums[left] + nums[right]

                if closest is None or abs(added - target) < abs(
                    closest - target
                ):
                    closest = added

                if added < target:
                    left += 1
                    continue
                elif added > target:
                    right -= 1
                    continue
                else:
                    closest = added
                    break

        return closest

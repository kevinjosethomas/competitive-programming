# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for index, num in enumerate(nums):
#             goal = target - num
#             try:
#                 ans = nums.index(goal)
#             except ValueError:
#                 continue

#             try:
#                 if ans == index:
#                     ans = nums.index(goal, ans+1)
#             except ValueError:
#                 continue

#             return index, ans


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapping = {}
        for index, num in enumerate(nums):

            if mapping.get(num):
                return index, mapping[num]

            goal = target - num
            mapping[goal] = index

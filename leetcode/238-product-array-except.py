from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        product_without_zero = 1
        for num in nums:
            product *= num
            if num != 0:
                product_without_zero *= num
            else:
                zero_count += 1

        answer = []
        for num in nums:
            if num == 0:
                answer.append(product_without_zero if zero_count == 1 else 0)
            else:
                answer.append(product // num)

        return answer

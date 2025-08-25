from typing import List


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        total = len(nums1) + len(nums2)

        for _ in range(((total // 2) - (1 if total % 2 == 0 else 0))):
            if not len(nums1):
                nums2.pop(0)
                continue

            if not len(nums2):
                nums1.pop(0)
                continue

            if nums1[0] <= nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)

        if total % 2 != 0:
            median = min(
                nums1[0] if len(nums1) else float("inf"),
                nums2[0] if len(nums2) else float("inf"),
            )
        else:
            x = 0
            for _ in range(2):
                if not len(nums1):
                    x += nums2.pop(0)
                    continue
                if not len(nums2):
                    x += nums1.pop(0)
                    continue
                if nums1[0] <= nums2[0]:
                    x += nums1.pop(0)
                else:
                    x += nums2.pop(0)
            median = x / 2

        return median

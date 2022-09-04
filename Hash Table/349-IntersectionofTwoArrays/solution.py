from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        return list(nums1_set & nums2_set)

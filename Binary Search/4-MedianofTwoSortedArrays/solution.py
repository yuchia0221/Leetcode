from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1)
        is_odd = (len(nums1) + len(nums2)) & 1
        left_size = (len(nums1) + len(nums2) + 1) // 2
        while left <= right:
            mid = (left + right) // 2
            remaining = left_size - mid

            nums1_left = nums1[mid-1] if mid > 0 else float("-inf")
            nums1_right = nums1[mid] if mid < len(nums1) else float("inf")
            nums2_left = nums2[remaining-1] if remaining > 0 else float("-inf")
            nums2_right = nums2[remaining] if remaining < len(nums2) else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if is_odd:
                    return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left, nums2_left)+min(nums1_right, nums2_right)) / 2
            elif nums2_left > nums1_right:
                left = mid + 1
            else:
                right = mid - 1

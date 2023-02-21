from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left+right) // 2
            is_first_half_even = (mid-left+1) % 2 == 0
            if nums[mid] == nums[mid+1]:
                if is_first_half_even:
                    right = mid - 1
                else:
                    left = mid + 2
            elif nums[mid-1] == nums[mid]:
                if is_first_half_even:
                    left = mid + 1
                else:
                    right = mid - 2
            else:
                return nums[mid]

        return nums[left]

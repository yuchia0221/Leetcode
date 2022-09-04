from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        left = number_of_subarray = 0
        for i, num in enumerate(nums):
            product *= num
            while product >= k:
                product /= nums[left]
                left += 1
            number_of_subarray += (i-left+1)

        return number_of_subarray

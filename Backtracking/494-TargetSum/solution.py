from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def helper(index: int, current_sum: int = 0) -> int:
            if index == len(nums):
                return int(current_sum == target)

            return helper(index+1, current_sum+nums[index]) + helper(index+1, current_sum-nums[index])

        return helper(0, 0)

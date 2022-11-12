from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dp(left, right):
            if right - left < 0:
                return 0

            result = 0
            for i in range(left, right + 1):
                gain = nums[left - 1] * nums[i] * nums[right + 1]
                remaining = dp(left, i - 1) + dp(i + 1, right)
                result = max(result, remaining + gain)
            return result

        nums = [1] + nums + [1]
        return dp(1, len(nums) - 2)

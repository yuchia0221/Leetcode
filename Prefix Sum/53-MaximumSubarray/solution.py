from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = 0
        for num in nums:
            current_sum = max(current_sum+num, num)
            max_sum = max(max_sum, current_sum)
        return max_sum

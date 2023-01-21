from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = min_sum = nums[0]
        total = current_max = current_min = 0

        for number in nums:
            current_max = max(current_max+number, number)
            max_sum = max(max_sum, current_max)
            current_min = min(current_min+number, number)
            min_sum = min(min_sum, current_min)
            total += number

        return max(max_sum, total-min_sum) if max_sum > 0 else max_sum

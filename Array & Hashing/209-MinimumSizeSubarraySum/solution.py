from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = slow = 0
        minimum_size = float("inf")
        for index, num in enumerate(nums):
            current_sum += num
            while current_sum >= target:
                if current_sum == target:
                    minimum_size = min(minimum_size, index-slow+1)
                current_sum -= nums[slow]
                slow += 1
        
        return minimum_size if minimum_size != float("inf") else 0

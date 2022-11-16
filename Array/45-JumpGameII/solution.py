from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        start = end = step = 0
        while end < len(nums) - 1:
            step += 1
            start, end = end+1, max(i+nums[i] for i in range(start, end+1))

        return step

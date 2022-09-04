from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for index, num in enumerate(nums):
            try:
                return [memo[num], index]
            except KeyError:
                memo[target-num] = index
        
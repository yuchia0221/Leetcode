from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(tempt: List[int], index: int):
            if len(tempt) <= len(nums):
                result.append(tempt)

            for i in range(index, len(nums)):
                helper(tempt+[nums[i]], i+1)

        result = []
        helper([], 0)
        return result

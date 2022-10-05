from collections import Counter
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(tempt: List[int], index: int):
            result.append(tempt)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                helper(tempt+[nums[i]], i+1)

        result = []
        nums.sort()
        helper([], 0)
        return result

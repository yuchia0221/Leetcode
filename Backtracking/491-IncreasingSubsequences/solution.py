from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def helper(tempt: List[int], index: int):
            if len(tempt) > 1:
                result.append(tempt)

            visited = set()
            for i in range(index, len(nums)):
                if tempt and tempt[-1] > nums[i] or nums[i] in visited:
                    continue
                visited.add(nums[i])
                helper(tempt+[nums[i]], i+1)

        result = []
        helper([], 0)
        return list(result)

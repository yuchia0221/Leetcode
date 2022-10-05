from typing import List
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(tempt: List[int], counter: Counter):
            if len(tempt) == len(nums):
                result.append(tempt[:])
                return

            for key, value in counter.items():
                if value > 0:
                    tempt.append(key)
                    counter[key] -= 1
                    helper(tempt, counter)
                    tempt.pop()
                    counter[key] += 1

        result = []
        helper([], Counter(nums))
        return result

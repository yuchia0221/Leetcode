from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(tempt: List[int], index: int):
            if len(tempt) == k:
                result.append(tempt[:])
                return

            for i in range(index, n+1):
                tempt.append(i)
                helper(tempt, i+1)
                tempt.pop()

        result = []
        helper([], 1)
        return result

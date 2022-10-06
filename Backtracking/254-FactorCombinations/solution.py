from math import sqrt
from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def helper(factors: List[int], least_factor: int, target: int):
            if len(factors) > 0:
                result.append(factors + [target])
            for candidate_factor in range(least_factor, int(sqrt(target))+1):
                if target % candidate_factor == 0:
                    helper(factors+[candidate_factor], candidate_factor, target // candidate_factor)

        result = []
        if n == 1:
            return result
        helper([], 2, n)
        return result

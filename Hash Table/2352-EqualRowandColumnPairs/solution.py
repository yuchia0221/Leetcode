from typing import List
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        memo = defaultdict(int)
        for row in grid:
            memo[tuple(row)] += 1

        equal_pairs = 0
        for col in zip(*grid):
            equal_pairs += memo[tuple(col)]

        return equal_pairs

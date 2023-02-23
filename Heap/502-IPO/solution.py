from heapq import heappop, heappush
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(capital, profits))
        max_heap = []
        pointer = 0
        for _ in range(k):
            while pointer < n and projects[pointer][0] <= w:
                heappush(max_heap, -projects[pointer][1])
                pointer += 1
            if not max_heap:
                break

            w += -heappop(max_heap)

        return w

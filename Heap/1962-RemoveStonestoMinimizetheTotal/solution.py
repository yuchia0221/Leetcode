import math
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapify(heap)

        for _ in range(k):
            pile = -heappop(heap)
            heappush(heap, -math.ceil(pile/2))

        return -sum(heap)

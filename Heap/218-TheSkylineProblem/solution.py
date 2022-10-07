from typing import List
from heapq import heappop, heappush


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        live, past = [], []
        edges, result = [], []
        for left, right, height in buildings:
            edges.append([left, height])
            edges.append([right, -height])
        edges.sort()
        index = 0
        while index < len(edges):
            current_x = edges[index][0]
            while index < len(edges) and edges[index][0] == current_x:
                height = edges[index][1]
                if height > 0:
                    heappush(live, -height)
                else:
                    heappush(past, height)

                index += 1

            while past and past[0] == live[0]:
                heappop(live)
                heappop(past)

            max_height = -live[0] if live else 0
            if not result or result[-1][1] != max_height:
                result.append([current_x, max_height])

        return result

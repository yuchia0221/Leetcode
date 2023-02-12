from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        def dfs(node: int) -> int:
            nonlocal answer
            subtree_size = 1
            for neighbor in graph[node]:
                if neighbor not in vistied:
                    vistied.add(node)
                    subtree_size += dfs(neighbor)
            if node != 0:
                answer += ceil(subtree_size / seats)
            return subtree_size

        graph = defaultdict(list)
        for src, dest in roads:
            graph[src].append(dest)
            graph[dest].append(src)

        answer = 0
        vistied = set()
        dfs(0)
        return answer

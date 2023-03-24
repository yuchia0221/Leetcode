from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(current: int, parent: int) -> int:
            nonlocal count
            for neighbor, is_origin_path in graph[current]:
                if neighbor != parent:
                    count += is_origin_path
                    dfs(neighbor, current)

        count = 0
        graph = defaultdict(list)
        for src, dest in connections:
            graph[src].append((dest, 1))
            graph[dest].append((src, 0))

        dfs(0, -1)
        return count

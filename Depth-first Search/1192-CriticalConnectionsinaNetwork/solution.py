from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def make_graph():
            for u, v in connections:
                graph[u].add(v)
                graph[v].add(u)
                critical_paths.add((min(u, v), max(u, v)))

        def dfs(node: int, timestamp: int) -> int:
            if rank[node]:
                return rank[node]

            rank[node] = timestamp
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == timestamp - 1:
                    continue
                back_depth = dfs(neighbor, timestamp+1)
                if back_depth <= timestamp:
                    critical_paths.remove((min(node, neighbor), max(node, neighbor)))
                min_back_depth = min(min_back_depth, back_depth)

            return min_back_depth

        rank = [None] * n
        critical_paths = set()
        graph = defaultdict(set)
        make_graph()
        dfs(0, 1)
        return list(critical_paths)

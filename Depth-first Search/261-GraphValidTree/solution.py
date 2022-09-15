from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        stack = [0]
        visited_nodes = set([0])
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor in visited_nodes:
                    continue
                visited_nodes.add(neighbor)
                stack.append(neighbor)

        return len(visited_nodes) == n

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node: int, path: List[int]) -> None:
            if node == target:
                paths.append(path)

            for neighbor in graph[node]:
                dfs(neighbor, path+[neighbor])

        paths = []
        target = len(graph)-1
        dfs(0, [0])
        return paths

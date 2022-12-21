from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(source: int) -> bool:
            queue = deque([source])
            color[source] = 0
            while queue:
                node = queue.pop()
                for neighbor in graph[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.appendleft(neighbor)
            return True

        if len(dislikes) == 0:
            return True

        graph = defaultdict(set)
        color = [-1 for _ in range(n+1)]

        for dislike in dislikes:
            src, dest = dislike
            graph[src].add(dest)
            graph[dest].add(src)

        for i in range(1, n+1):
            if color[i] == -1 and not bfs(i):
                return False

        return True

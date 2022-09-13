from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(row: int, column: int) -> bool:
            if [row, column] == destination:
                return True
            else:
                for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                    x, y = row, column
                    while 0 <= x+dx < len(maze) and 0 <= y+dy < len(maze[0]) and not maze[x+dx][y+dy]:
                        x, y = x+dx, y+dy
                    if (x, y) not in has_seen:
                        has_seen.add((x, y))
                        if dfs(x, y):
                            return True
            return False

        has_seen = set()
        return dfs(*start)

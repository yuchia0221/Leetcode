from collections import deque
from dataclasses import dataclass
from typing import List


@dataclass
class SearchStep:
    row: int
    column: int
    step: int

    def get_location(self) -> List[int]:
        return (self.row, self.column)


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        distance = {tuple(start): 0}
        shortest_path = float("inf")
        row_number, col_number = len(maze), len(maze[0])
        queue = deque([SearchStep(start[0], start[1], 0)])
        while queue:
            current_status = queue.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = current_status.get_location()
                step = current_status.step
                while 0 <= x+dx < row_number and 0 <= y+dy < col_number and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    step += 1

                if [x, y] == destination:
                    shortest_path = min(shortest_path, step)
                    continue

                if ((x, y) in distance and distance[(x, y)] > step) or (x, y) not in distance:
                    distance[(x, y)] = step
                    queue.append(SearchStep(x, y, step))

        return shortest_path if shortest_path != float("inf") else -1

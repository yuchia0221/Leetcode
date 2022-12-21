# The Maze II

Problem can be found in [here](https://leetcode.com/problems/the-maze-ii/)!

### [Solution](/Breadth-first%20Search/505-TheMazeII/solution.py): Breadth-first Search

```python
@dataclass
class SearchStep:
    row: int
    column: int
    step: int

    def get_location(self) -> List[int]:
        return (self.row, self.column)


def shortestDistance(maze: List[List[int]], start: List[int], destination: List[int]) -> int:
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
```

Explanation: When we perform BFS, we just need to store the steps we take so far to reach this position. Also, we should only push item into queue if and only if we find a shorter path to this point.

Time Complexity: ![O(nm*max(n,m))](<https://latex.codecogs.com/svg.image?O(nm\cdot&space;max(n,m))>), Space Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), where n and m is the number of row and column, respectively.

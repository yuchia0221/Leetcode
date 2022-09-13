# The Maze

Problem can be found in [here](https://leetcode.com/problems/the-maze/)!

### [Solution](/Depth-first%20Search/490-TheMaze/solution.py): Depth-first Search

```python
def hasPath(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
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
```

Explanation: Perform DFS until we reach the destination or we visited all of the nodes.

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), where n and m is the number of row and column, respectively.

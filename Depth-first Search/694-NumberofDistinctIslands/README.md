# Number of Distinct Islands

Problem can be found in [here](https://leetcode.com/problems/number-of-distinct-islands/)!

### [Solution](/Depth-first%20Search/694-NumberofDistinctIslands/solution.py): Depth-first Search + Hash Table

```python
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.grid = grid
        island_shape_memo = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.grid[row][col] == 1:
                    island_shape = self.dfs(row, col, [])
                    island_shape_memo.add("".join(island_shape))

        return len(island_shape_memo)

    def dfs(self, row: int, column: int, shape: List[str]) -> List[str]:
        self.grid[row][column] = 0
        for dx, dy, direction in ((1, 0, "l"), (-1, 0, "r"), (0, 1, "t"), (0, -1, "d")):
            new_row, new_col = row+dx, column+dy
            in_bounaries = 0 <= new_row < len(self.grid) and 0 <= new_col < len(self.grid[0])
            if in_bounaries and self.grid[new_row][new_col] == 1:
                shape.append(direction)
                self.dfs(new_row, new_col, shape)

        shape.append("#")
        return shape
```

Explanation: We just need to slightly modify the solution of [Number of Islands](https://leetcode.com/problems/number-of-islands/). In each DFS iteration, we need to track the direction of our traversal and push it into the hash table. If there is a match in the hash table, we know it is a duplicated island.

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), where n and m is the number of row and column, respectively.

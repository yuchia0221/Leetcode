# Minimum Path Sum

Problem can be found in [here](https://leetcode.com/problems/minimum-path-sum/)!

### [Solution](/Dynamic%20Programming/64-MinimumPathSum/solution.py): Dynamic Programming

```python
def minPathSum(grid: List[List[int]]) -> int:
    row_length, col_length = len(grid), len(grid[0])

    for row in range(row_length):
        for col in range(col_length):
            if row == 0 and col == 0:
                continue
            elif row == 0:
                grid[row][col] += grid[row][col-1]
            elif col == 0:
                grid[row][col] += grid[row-1][col]
            else:
                grid[row][col] += min(grid[row][col-1], grid[row-1][col])

    return grid[-1][-1]
```

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n and m is the number of row and column, respectively.

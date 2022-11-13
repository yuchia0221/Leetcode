# Unique Path II

Problem can be found in [here](https://leetcode.com/problems/unique-paths-ii/)!

### [Solution](/Dynamic%20Programming/63-UniquePathsII/solution.py): Dynamic Programming

```python
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    row_length, col_length = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * col_length
    dp[0] = 1 - obstacleGrid[0][0]
    for col in range(1, col_length):
        dp[col] = dp[col-1] * (1 - obstacleGrid[0][col])

    for row in range(1, row_length):
        dp[0] *= (1 - obstacleGrid[row][0])
        for col in range(1, col_length):
            dp[col] = (dp[col] + dp[col-1]) * (1 - obstacleGrid[row][col])

    return dp[-1]
```

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(m)](<https://latex.codecogs.com/svg.image?\inline&space;O(m)>), where n and m is the number of row and column, respectively.

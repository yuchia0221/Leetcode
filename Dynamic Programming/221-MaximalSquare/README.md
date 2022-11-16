# Maximal Square

Problem can be found in [here](https://leetcode.com/problems/maximal-square/)!

### [Solution](/Dynamic%20Programming/221-MaximalSquare/solution.py): Dynamic Programming

```python
def maximalSquare(matrix: List[List[str]]) -> int:
    prev = max_square_length = 0
    row_length, col_length = len(matrix), len(matrix[0])
    dp = [0] * col_length

    for row in range(row_length):
        for col in range(col_length):
            tempt = dp[col]
            if matrix[row][col] == "1":
                if row != 0 and col != 0 and matrix[row-1][col-1] == "1":
                    dp[col] = min(dp[col], dp[col-1], prev) + 1
                else:
                    dp[col] = 1
                max_square_length = max(max_square_length, dp[col])
            else:
                dp[col] = 0

            prev = tempt

    return max_square_length * max_square_length
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

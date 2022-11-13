from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
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

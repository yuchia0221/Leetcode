from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
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

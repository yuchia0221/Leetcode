from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
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

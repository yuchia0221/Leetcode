from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int) -> int:
            if not (0 <= row < row_num and 0 <= col < col_num):
                return 0
            if grid[row][col] != 1:
                return 0

            grid[row][col] = -1
            current_area = 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)
            return current_area

        max_area = 0
        row_num, col_num = len(grid), len(grid[0])
        for row in range(row_num):
            for col in range(col_num):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area

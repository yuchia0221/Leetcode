from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int, unvisited: int) -> None:
            nonlocal path_num
            if grid[row][col] == 2 and unvisited == 1:
                path_num += 1
                return

            unvisited -= 1
            grid[row][col], tempt = -4, grid[row][col]
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_row, next_col = row+dx, col+dy
                if not (0 <= next_row < row_num and 0 <= next_col < col_num):
                    continue
                if grid[next_row][next_col] < 0:
                    continue
                dfs(next_row, next_col, unvisited)

            grid[row][col] = tempt

        row_num, col_num = len(grid), len(grid[0])
        start_row = start_col = unvisited = path_num = 0

        for row in range(row_num):
            for col in range(col_num):
                value = grid[row][col]
                if value >= 0:
                    unvisited += 1
                if value == 1:
                    start_row, start_col = row, col

        dfs(start_row, start_col, unvisited)
        return path_num

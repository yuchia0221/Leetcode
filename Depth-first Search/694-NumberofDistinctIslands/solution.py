from typing import List


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

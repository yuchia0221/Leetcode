from typing import List


class Solution:
    def solveNQueens(self, n):
        def helper(queens_left: int, row: int):
            if queens_left == 0:
                result.append(self.create_output_board(board))
                return

            for col in range(n):
                diagonal, antidiagonal = row - col, row + col
                if col in used_cols or diagonal in used_diagonals or antidiagonal in used_antidiagonals:
                    continue

                used_cols.add(col)
                used_diagonals.add(diagonal)
                used_antidiagonals.add(antidiagonal)
                board[row][col] = "Q"

                helper(queens_left-1, row+1)

                used_cols.remove(col)
                used_diagonals.remove(diagonal)
                used_antidiagonals.remove(antidiagonal)
                board[row][col] = "."

        used_cols = set()
        used_diagonals = set()
        used_antidiagonals = set()

        result = []
        board = [["."] * n for _ in range(n)]
        helper(n, 0)
        return result

    def create_output_board(self, board: List[List[str]]):
        return ["".join(row) for row in board]

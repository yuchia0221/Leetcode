from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        row_num, col_num = len(board), len(board[0])
        offset = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        for row in range(row_num):
            for col in range(col_num):
                live_neighbors = 0
                for dx, dy in offset:
                    is_in_boundaires = (0 <= row+dx <= row_num-1) and (0 <= col+dy <= col_num-1)
                    if is_in_boundaires and (board[row+dx][col+dy] == 1 or board[row+dx][col+dy] == -1):
                        live_neighbors += 1

                if live_neighbors < 2 and board[row][col] == 1:
                    board[row][col] = -1
                elif live_neighbors > 3 and board[row][col] == 1:
                    board[row][col] = -1
                elif live_neighbors == 3 and board[row][col] == 0:
                    board[row][col] = 2

        for row in range(row_num):
            for col in range(col_num):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1

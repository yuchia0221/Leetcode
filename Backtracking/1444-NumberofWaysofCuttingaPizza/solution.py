from functools import cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        row_num, col_num = len(pizza), len(pizza[0])
        remaining_graph = [[0] * (col_num+1) for _ in range(row_num+1)]
        for row in range(row_num-1, -1, -1):
            for col in range(col_num-1, -1, -1):
                remaining_graph[row][col] = remaining_graph[row+1][col] + \
                    remaining_graph[row][col+1] - remaining_graph[row+1][col+1] + (pizza[row][col] == "A")

        @cache
        def backtracking(row: int, col: int, cut_remained: int) -> int:
            if remaining_graph[row][col] == 0:
                return 0
            if cut_remained == 0:
                return 1

            answer = 0
            for new_row in range(row+1, row_num):
                if remaining_graph[row][col] - remaining_graph[new_row][col] > 0:
                    answer += backtracking(new_row, col, cut_remained-1)

            for new_col in range(col+1, col_num):
                if remaining_graph[row][col] - remaining_graph[row][new_col] > 0:
                    answer += backtracking(row, new_col, cut_remained-1)

            return answer

        return backtracking(0, 0, k-1) % (pow(10, 9)+7)

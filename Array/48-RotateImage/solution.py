from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose():
            for row in range(n):
                for col in range(row+1, n):
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        def reflect():
            for row in range(n):
                for col in range(n // 2):
                    matrix[row][col], matrix[row][-col-1] = matrix[row][-col-1], matrix[row][col]

        n = len(matrix)
        transpose()
        reflect()
        return

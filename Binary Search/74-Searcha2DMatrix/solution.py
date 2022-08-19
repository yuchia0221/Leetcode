from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, column = len(matrix), len(matrix[0])
        left, right = 0, row*column - 1
        while left <= right:
            mid = (left+right) // 2
            row_number, column_number = mid // column, mid % column
            candidate = matrix[row_number][column_number]
            if candidate == target:
                return True
            elif candidate > target:
                right = mid - 1
            else:
                left = mid + 1

        return False

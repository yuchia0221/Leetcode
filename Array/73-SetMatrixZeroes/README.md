# Set Matrix Zeroes

Problem can be found in [here](https://leetcode.com/problems/set-matrix-zeroes/)!

### [Solution](/Array/73-SetMatrixZeroes/solution.py)

```python
def setZeroes(matrix: List[List[int]]) -> None:
    def set_flags() -> bool:
        is_first_col_zero = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                is_first_col_zero = True

            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = matrix[0][col] = 0

        return is_first_col_zero

    def tranform_matrix_with_flags():
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

        if is_first_col_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0

    is_first_col_zero = set_flags()
    tranform_matrix_with_flags()
    return
```

Time Complexity: ![O(mn)](<https://latex.codecogs.com/svg.image?\inline&space;O(mn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

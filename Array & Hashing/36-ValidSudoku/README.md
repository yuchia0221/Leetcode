# Valid Sudoku

Problem can be found in [here](https://leetcode.com/problems/valid-sudoku/)!

### [Solution](/Array%20%26%20Hashing/36-ValidSudoku/solution.py): Hash Table

```python
def isValidSudoku(board: List[List[str]]) -> bool:
    def check_columns() -> bool:
        for column in zip(*board):
            if not check_unit(column):
                return False
        return True

    def check_rows() -> bool:
        for row in board:
            if not check_unit(row):
                return False
        return True

    def check_sub_boxes() -> bool:
        for row in range(0, len(board), 3):
            for column in range(0, len(board[0]), 3):
                numbers = [board[x][y] for x in range(row, row+3) for y in range(column, column+3)]
                if not check_unit(numbers):
                    return False
        return True

    def check_unit(unit: List[int]) -> bool:
        unit = [i for i in unit if i != "."]
        return len(set(unit)) == len(unit)

    is_board_valid = check_columns() and check_rows() and check_sub_boxes()
    return is_board_valid
```

Explanation: There is no shortcut, so we have to check every column, every row, and every 9\*9 sub-boxes for a valid sudoku.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

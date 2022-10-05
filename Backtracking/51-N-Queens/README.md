# N-Queens

Problem can be found in [here](https://leetcode.com/problems/n-queens/)!

### [Solution](/Backtracking/51-N-Queens/solution.py): Backtracking

```python
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
```

Explanation: The main idea of solving this solution is to use backtracking algorithm. The hard part is to observe the properties of diagonal and anti-diagonal, which elements in the same diagonal share same row-col while elements in the same anti-diagonal share same row+col. We can use set to track which col, diagonal, and anti-diagonal we use to place a queen in the board efficiently. 

Time Complexity: ![O(n!)](<https://latex.codecogs.com/svg.image?\inline&space;O(n!)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the number of queens.

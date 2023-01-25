from collections import deque
from typing import List, Tuple


def label_to_position(label: int, n: int) -> Tuple[int]:
    row, col = divmod(label-1, n)
    if row % 2 == 0:
        return n-row-1, col
    else:
        return n-row-1, n-col-1


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        seen = set()
        queue = deque([(1, 0)])

        while queue:
            label, step = queue.popleft()
            row, col = label_to_position(label, n)
            if board[row][col] != -1:
                label = board[row][col]
            if label == n*n:
                return step
            for dx in range(1, 7):
                new_label = label + dx
                if new_label <= n*n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step+1))

        return -1

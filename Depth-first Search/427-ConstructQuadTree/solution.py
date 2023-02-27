from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        self.grid = grid
        return self.helper(0, 0, len(grid))

    def helper(self, row: int, col: int, length: int) -> "Node":
        if length == 1:
            return Node(self.grid[row][col] != 0, True)

        half_length = length // 2
        top_left = self.helper(row, col, half_length)
        top_right = self.helper(row, col + half_length, half_length)
        bottom_left = self.helper(row + half_length, col, half_length)
        bottom_right = self.helper(row + half_length, col + half_length, half_length)

        if self.check_can_combine(top_left, top_right, bottom_left, bottom_right):
            return Node(top_left.val, True)
        else:
            return Node(False, False, top_left, top_right, bottom_left, bottom_right)

    def check_can_combine(self, top_left: "Node", top_right: "Node", bottom_left: "Node", bottom_right: "Node") -> bool:
        is_leaf = top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf
        same_value = len(set([top_left.val, top_right.val, bottom_left.val, bottom_right.val])) == 1

        return is_leaf and same_value

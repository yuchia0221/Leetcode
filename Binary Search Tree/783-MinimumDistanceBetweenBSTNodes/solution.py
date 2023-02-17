from operator import index
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    previous, result = -float("inf"), float("inf")

    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None:
            return

        self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.previous)
        self.previous = root.val

        self.minDiffInBST(root.right)
        return self.result

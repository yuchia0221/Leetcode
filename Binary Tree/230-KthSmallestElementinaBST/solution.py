from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder_result = []
        self.inorder_traversal(root)
        return self.inorder_result[k-1]

    def inorder_traversal(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.inorder_traversal(root.left)
        self.inorder_result.append(root.val)
        self.inorder_traversal(root.right)

from operator import index
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(node: Optional[TreeNode]) -> None:
            nonlocal nodes
            if not node:
                return

            inorder_traversal(node.left)
            nodes.append(node.val)
            inorder_traversal(node.right)

        nodes = []
        inorder_traversal(root)

        min_difference = float("inf")
        for i in range(1, len(nodes)):
            min_difference = min(nodes[i]-nodes[i-1], min_difference)

        return min_difference

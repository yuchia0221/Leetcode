from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.traversalHelper(root)
        return self.result

    def traversalHelper(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.traversalHelper(root.left)
        self.traversalHelper(root.right)
        self.result.append(root.val)

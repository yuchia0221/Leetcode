from operator import index
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.index = -1
        self.inorder_result = []
        self.inorder_traversal(root)
        self.tree_length = len(self.inorder_result)

    def inorder_traversal(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.inorder_traversal(root.left)
        self.inorder_result.append(root)
        self.inorder_traversal(root.right)

    def next(self) -> int:
        self.index += 1
        return self.inorder_result[self.index].val

    def hasNext(self) -> bool:
        return True if self.index != self.tree_length - 1 else False

from re import L
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal postorder_index
            if left > right:
                return None
            elif left == right:
                root = TreeNode(postorder[postorder_index])
                postorder_index -= 1
                return root
            else:
                root = TreeNode(postorder[postorder_index])
                postorder_index -= 1
                preorder_index = preorder_memo[postorder[postorder_index]]
                root.right = array_to_tree(preorder_index, right)
                root.left = array_to_tree(left+1, preorder_index-1)
                return root

        preorder_memo = {}
        postorder_index = len(postorder)-1
        for index, value in enumerate(preorder):
            preorder_memo[value] = index

        return array_to_tree(0, len(preorder)-1)

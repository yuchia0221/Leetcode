from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float("-inf")
        self.one_path_sum(root)
        return self.max_path_sum

    def one_path_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_path_sum = max(0, self.one_path_sum(root.left))
        right_path_sum = max(0, self.one_path_sum(root.right))
        self.max_path_sum = max(self.max_path_sum, root.val+left_path_sum+right_path_sum)
        return max(left_path_sum, right_path_sum) + root.val

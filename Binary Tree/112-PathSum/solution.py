from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = deque([[root, targetSum-root.val]])
        while queue:
            node, current_sum = queue.popleft()
            left_node, right_node = node.left, node.right
            if not left_node and not right_node and current_sum == 0:
                return True
            if left_node:
                queue.append([left_node, current_sum-left_node.val])
            if right_node:
                queue.append([right_node, current_sum-right_node.val])

        return False

from typing import Optional
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxLevelSum(root: Optional[TreeNode]) -> int:
    queue = deque([root])
    max_level_sum = float("-inf")
    current_level = max_level = 0

    while queue:
        current_level += 1
        current_level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            current_level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if current_level_sum > max_level_sum:
            max_level_sum = current_level_sum
            max_level = current_level

    return max_level

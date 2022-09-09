from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output_list = []
        left_2_right = True
        queue = deque([root])
        while queue:
            tempt = []
            for _ in range(len(queue)):
                if left_2_right:
                    node = queue.popleft()
                    tempt.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    tempt.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)

            left_2_right = not left_2_right
            output_list.append(tempt)

        return output_list

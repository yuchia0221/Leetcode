# Minimum Distance Between BST Nodes

Problem can be found in [here](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Search%20Tree/783-MinimumDistanceBetweenBSTNodes/solution.py): Inorder Traversal

```python
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

# Minimum Absolute Difference in BST

Problem can be found in [here](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Search%20Tree/530-MinimumAbsoluteDifferenceinBST/solution.py): Inorder Traversal

```python
def getMinimumDifference(root: Optional[TreeNode]) -> int:
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

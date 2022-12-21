# Flatten Binary Tree to Linked List

Problem can be found in [here](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/114-FlattenBinaryTreetoLinkedList/solution.py)

```python

```
def flatten(self, root: Optional[TreeNode]) -> None:
    if not root:
        return None

    node = root
    while node:
        if node.left:
            rightmost = node.left
            while rightmost.right:
                rightmost = rightmost.right

            rightmost.right = node.right
            node.right = node.left
            node.left = None

        node = node.right
Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

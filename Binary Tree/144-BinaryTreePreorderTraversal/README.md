# Binary Tree Preorder Traversal

Problem can be found in [here](https://leetcode.com/problems/binary-tree-preorder-traversal/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/144-BinaryTreePreorderTraversal/solution.py): Recursion

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.traversalHelper(root)
        return self.result

    def traversalHelper(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.result.append(root.val)
        self.traversalHelper(root.left)
        self.traversalHelper(root.right)
```

Explanation: Preorfer traversal visits root → left node → right node

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

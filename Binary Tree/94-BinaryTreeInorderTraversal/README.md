# Binary Tree Inorder Traversal

Problem can be found in [here](https://leetcode.com/problems/binary-tree-inorder-traversal/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/94-BinaryTreeInorderTraversal/solution.py): Recursion

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.traversalHelper(root)
        return self.result

    def traversalHelper(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.traversalHelper(root.left)
        self.result.append(root.val)
        self.traversalHelper(root.right)
```

Explanation: In-order traversal visits left node → root → right node.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

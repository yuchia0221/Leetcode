# Binary Tree Postorder Traversal

Problem can be found in [here](https://leetcode.com/problems/binary-tree-postorder-traversal/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/145-BinaryTreePostorderTraversal/solution.py): Recursion

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.traversalHelper(root)
        return self.result

    def traversalHelper(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.traversalHelper(root.left)
        self.traversalHelper(root.right)
        self.result.append(root.val)
```

Explanation: Postorfer traversal visits left node → right node → root

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

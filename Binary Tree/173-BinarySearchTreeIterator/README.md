# Binary Search Tree Iterator

Problem can be found in [here](https://leetcode.com/problems/binary-search-tree-iterator/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/173-BinarySearchTreeIterator/solution.py): Inorder Traversal

```python
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.index = -1
        self.inorder_result = []
        self.inorder_traversal(root)
        self.tree_length = len(self.inorder_result)

    def inorder_traversal(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.inorder_traversal(root.left)
        self.inorder_result.append(root)
        self.inorder_traversal(root.right)

    def next(self) -> int:
        self.index += 1
        return self.inorder_result[self.index].val

    def hasNext(self) -> bool:
        return True if self.index != self.tree_length - 1 else False
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

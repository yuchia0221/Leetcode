# Kth Smallest Element in a BST

Problem can be found in [here](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)!

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
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    inorder_result = []
    inorder_traversal(root, inorder_result)
    return inorder_result[k-1]

def inorder_traversal(root: Optional[TreeNode], result: List[int]) -> None:
    if not root:
        return

    inorder_traversal(root.left)
    inorder_result.append(root.val)
    inorder_traversal(root.right)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

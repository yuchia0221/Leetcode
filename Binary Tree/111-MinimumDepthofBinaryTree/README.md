# Minimum Depth of Binary Tree

Problem can be found in [here](https://leetcode.com/problems/minimum-depth-of-binary-tree/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/111-MinimumDepthofBinaryTree/solution.py)

```python
def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    if not root.left or not root.right:
        return max(minDepth(root.left), minDepth(root.right)) + 1
    else:
        return min(.minDepth(root.left), minDepth(root.right)) + 1
```

Explanation: We can simply use recursion to solve this problem. There are three cases to handle. First, if we are at the leaf node (root is None), then we can simply return 0. Next, if are not in the leaf node and there is at least one child is None, we should return the depth of the non-empty subtree. For example, if left child is None, we should calculate the depth of right subtree.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

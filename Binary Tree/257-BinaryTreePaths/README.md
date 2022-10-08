# Binary Tree Paths

Problem can be found in [here](https://leetcode.com/problems/binary-tree-paths/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/257-BinaryTreePaths/solution.py): Depth-first Search

```python
def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    def dfs(node: Optional[TreeNode], path: List[str]):
        if not node.left and not node.right:
            result.append("->".join(path+[str(node.val)]))
            return

        if node.left:
            dfs(node.left, path+[str(node.val)])
        if node.right:
            dfs(node.right, path+[str(node.val)])

    result = []
    dfs(root, [])
    return result
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where is the number of nodes in the binary tree.

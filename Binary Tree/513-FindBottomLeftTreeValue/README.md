# Find Bottom Left Tree Value

Problem can be found in [here](https://leetcode.com/problems/find-bottom-left-tree-value/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/513-FindBottomLeftTreeValue/solution.py): Breadth-First Search

```python
def findBottomLeftValue(root: Optional[TreeNode]) -> int:
    queue = deque([root])
    leftmost_node = None
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i == 0:
                leftmost_node = node.val

    return leftmost_node
```

Explanation: The problem ask us to return the value of the leftmost tree node in the binary tree. To solve this problem, we can perform breadth-first search to traverse each level. In each level traversal, we will update the value of leftmost tree node.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

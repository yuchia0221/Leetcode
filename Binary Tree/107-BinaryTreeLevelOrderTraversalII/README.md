# Binary Tree Level Order Traversal II

Problem can be found in [here](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/107-BinaryTreeLevelOrderTraversalII/solution.py): Breadth-First Search

```python
def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
      if not root:
          return []

      queue = deque([root])
      nodes_each_level = []
      while queue:
          tempt = []
          for _ in range(len(queue)):
              node = queue.popleft()
              tempt.append(node.val)
              if node.left:
                  queue.append(node.left)
              if node.right:
                  queue.append(node.right)
          nodes_each_level.append(tempt)

      return nodes_each_level[::-1]
```

Explanation: Just perform a breadth-first search and reverse the traversal result.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

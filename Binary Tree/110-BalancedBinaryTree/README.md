# Balanced Binary Tree

Problem can be found in [here](https://leetcode.com/problems/same-tree/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/100-SameTree/solution.py): Recursion

```python
def isBalanced(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True

    memo = {}
    is_root_balanced = abs(find_depth(memo, root.left)-find_depth(memo, root.right)) <= 1
    return is_root_balanced and isBalanced(root.left) and isBalanced(root.right)

def find_depth(memo: Dict[TreeNode], node: Optional[TreeNode]) -> int:
    if node is None:
        return 0
    if node not in memo:
        memo[node] = max(find_depth(node.left), find_depth(node.right)) + 1

    return memo[node]
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

# Binary Tree Maximum Path Sum

Problem can be found in [here](https://leetcode.com/problems/binary-tree-maximum-path-sum/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/124-BinaryTreeMaximumPathSum/solution.py): Depth-first Search

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float("-inf")
        self.one_path_sum(root)
        return self.max_path_sum

    def one_path_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_path_sum = max(0, self.one_path_sum(root.left))
        right_path_sum = max(0, self.one_path_sum(root.right))
        self.max_path_sum = max(self.max_path_sum, root.val+left_path_sum+right_path_sum)
        return max(left_path_sum, right_path_sum) + root.val
```

Explnation: The question is looking at the maximum path sum given a pair of two nodes. Suppose we have a function called one_path_sum that calculate the maximum path sum of given root. For each node, the maximum path sum including passing this node: node.val + max(0, one_path_sum(node.left))+max(0, one_path_sum(node.right)) . The reason why we need to use the max operation is because we can choose not to include this path since path sum may be negative.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

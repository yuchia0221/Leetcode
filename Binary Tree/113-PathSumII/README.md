# PathSum II

Problem can be found in [here](https://leetcode.com/problems/path-sum-ii/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/113-PathSumII/solution.py): Breadth-first Search

```python
def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    if not root:
        return []

    paths = []
    queue = deque([[root, [root.val], targetSum-root.val]])
    while queue:
        node, path, current_sum = queue.popleft()
        left_node, right_node = node.left, node.right
        if not left_node and not right_node and current_sum == 0:
            paths.append(path)
        if left_node:
            queue.append([left_node, path+[left_node.val], current_sum-left_node.val])
        if right_node:
            queue.append([right_node, path+[right_node.val], current_sum-right_node.val])

    return paths
```

Explanation: Slightly modify the answer in [Path Sum](/Binary%20Tree/112-PathSum/) and pass another variable storing the whole path from the root. If we find there is a match, then append it into the answer.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

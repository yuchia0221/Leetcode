# Construct Binary Tree from Inorder and Postorder Traversal

Problem can be found in [here](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/106-ConstructBinaryTreefromInorderandPostorderTraversal/solution.py)

```python
def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
        nonlocal postorder_index
        if left > right:
            return None

        root = TreeNode(postorder[postorder_index])
        postorder_index -= 1
        inorder_index = inorder_memo[root.val]
        root.right = array_to_tree(inorder_index+1, right)
        root.left = array_to_tree(left, inorder_index-1)
        return root

    inorder_memo = {}
    postorder_index = len(postorder)-1
    for index, value in enumerate(inorder):
        inorder_memo[value] = index

    return array_to_tree(0, len(postorder)-1)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

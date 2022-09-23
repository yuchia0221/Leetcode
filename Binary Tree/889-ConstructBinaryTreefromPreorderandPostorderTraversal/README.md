# Construct Binary Tree from Preorder and Postorder Traversal

Problem can be found in [here](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)!

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### [Solution](/Binary%20Tree/889-ConstructBinaryTreefromPreorderandPostorderTraversal/solution.py)

```python
def constructFromPrePost(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
        nonlocal postorder_index
        if left > right:
            return None
        elif left == right:
            root = TreeNode(postorder[postorder_index])
            postorder_index -= 1
            return root
        else:
            root = TreeNode(postorder[postorder_index])
            postorder_index -= 1
            preorder_index = preorder_memo[postorder[postorder_index]]
            root.right = array_to_tree(preorder_index, right)
            root.left = array_to_tree(left+1, preorder_index-1)
            return root

    preorder_memo = {}
    postorder_index = len(postorder)-1
    for index, value in enumerate(preorder):
        preorder_memo[value] = index

    return array_to_tree(0, len(preorder)-1)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

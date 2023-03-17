class Solution:
    def dfs(self, node: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not node:
            return None

        if node in self.nodes:
            return self.nodes[node]

        new_root = NodeCopy(node.val)
        self.nodes[node] = new_root

        new_root.left = self.dfs(node.left)
        new_root.right = self.dfs(node.right)
        new_root.random = self.dfs(node.random)

        return new_root

    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        self.nodes = {}
        new_root = self.dfs(root)
        return new_root

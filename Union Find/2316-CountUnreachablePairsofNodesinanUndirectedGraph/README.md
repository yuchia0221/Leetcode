# Count Unreachable Pairs of Nodes in an Undirected Graph

Problem can be found in [here](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/)!

### [Solution](/Union%20Find/2316-CountUnreachablePairsofNodesinanUndirectedGraph/solution.py): Disjoint Set

```python
class DisjointSet:
    def __init__(self, n: int):
        self.size = [1] * n
        self.parent = list(range(n))
        self.unreachable_pairs = n*(n-1) // 2

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u: int, v: int) -> None:
        u_root, v_root = self.find(u), self.find(v)

        if u_root == v_root:
            return

        self.unreachable_pairs -= self.size[u_root] * self.size[v_root]
        if self.size[u_root] >= self.size[v_root]:
            self.parent[v_root] = u_root
            self.size[u_root] += self.size[v_root]
        else:
            self.parent[u_root] = v_root
            self.size[v_root] += self.size[u_root]


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        disjoint_set = DisjointSet(n)
        for src, dest in edges:
            disjoint_set.union(src, dest)

        return disjoint_set.unreachable_pairs
```

Time Complexity: ![O(m*a(n))](<https://latex.codecogs.com/svg.image?\inline&space;O(m\cdot&space;\alpha&space;(n))>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where m is the length of array edges and $\alpha(\cdot)$ is the inverse ackermann function, which grows slowl.

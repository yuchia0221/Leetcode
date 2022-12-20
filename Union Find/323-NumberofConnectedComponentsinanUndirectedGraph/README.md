# Number of Connected Components in an Undirected Graph

Problem can be found in [here](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)!

### [Solution](/Union%20Find/305-NumberofIslandsII/solution.py): Disjoint Set

```python
class DisjointSet:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, u: int, v: int):
        u_root, v_root = self.find(u), self.find(v)

        if self.rank[u_root] == self.rank[v_root]:
            self.rank[u_root] += 1
            self.parent[v_root] = u_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[u_root] = v_root


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components_num = n
        disjoint_set = DisjointSet(n)
        for edge in edges:
            src, dest = edge
            if disjoint_set.find(src) != disjoint_set.find(dest):
                disjoint_set.union(src, dest)
                components_num -= 1

        return components_num
```

Time Complexity: ![O(E*a(V))](<https://latex.codecogs.com/svg.image?\inline&space;O(E\cdot&space;\alpha&space;(V))>), Space Complexity: ![O(V)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), where E and V are the number of edges and vertices, respectively.

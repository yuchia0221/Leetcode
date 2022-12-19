# Find if Path Exists in Graph

Problem can be found in [here](https://leetcode.com/problems/find-if-path-exists-in-graph/)!

### [Solution](/Union%20Find/1971-FindifPathExistsinGraph/solution.py): Disjoint Set

```python
class DisjointSet:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.ranks = [1 for _ in range(n)]

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, u: int, v: int):
        u_root, v_root = self.find(u), self.find(v)

        if self.ranks[u_root] == self.ranks[v_root]:
            self.parents[v_root] = u_root
            self.ranks[u_root] += 1
        elif self.ranks[u_root] > self.ranks[v_root]:
            self.parents[v_root] = u_root
        else:
            self.parents[u_root] = v_root


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        disjoint_set = DisjointSet(n)

        for edge in edges:
            src, dest = edge
            disjoint_set.union(src, dest)

        return disjoint_set.find(source) == disjoint_set.find(destination)
```

Time Complexity: ![O(m*a(n))](<https://latex.codecogs.com/svg.image?\inline&space;O(m\cdot&space;\alpha&space;(n))>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where m is the number of edges and $\alpha(\cdot)$ is the inverse ackermann function, which grows slowly, and n is the number of vertices.

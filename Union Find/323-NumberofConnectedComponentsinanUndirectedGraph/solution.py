from typing import List


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

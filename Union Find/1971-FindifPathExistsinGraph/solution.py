from typing import List


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

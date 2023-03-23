from typing import List


class DisjointSet:
    def __init__(self, n: int):
        self.components = n
        self.rank = [1] * n
        self.parent = list(range(n))

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u: int, v: int) -> None:
        u_root, v_root = self.find(u), self.find(v)

        if u_root == v_root:
            return

        self.components -= 1
        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        elif self.rank[u_root] == self.rank[v_root]:
            self.rank[u_root] += 1
            self.parent[v_root] = u_root
        else:
            self.parent[u_root] = v_root


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        disjoint_set = DisjointSet(n)
        for src, dest in connections:
            disjoint_set.union(src, dest)

        return disjoint_set.components - 1

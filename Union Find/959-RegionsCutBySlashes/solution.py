from typing import List


class DisjointSet:
    def __init__(self, num: int):
        self.components = num
        self.rank = [1] * num
        self.parent = list(range(num))

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u: int, v: int):
        u_root, v_root = self.find(u), self.find(v)

        if u_root == v_root:
            return

        self.components -= 1
        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        elif self.rank[u_root] == self.rank[v_root]:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        else:
            self.parent[u_root] = v_root


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        disjoint_set = DisjointSet(4 * N * N)
        for row in range(N):
            for col in range(N):
                val, root = grid[row][col], 4 * (row*N + col)
                if val in '/ ':
                    disjoint_set.union(root + 0, root + 1)
                    disjoint_set.union(root + 2, root + 3)
                if val in '\ ':
                    disjoint_set.union(root + 0, root + 2)
                    disjoint_set.union(root + 1, root + 3)

                if row+1 < N:
                    disjoint_set.union(root + 3, (root+4*N) + 0)
                if row-1 >= 0:
                    disjoint_set.union(root + 0, (root-4*N) + 3)
                if col+1 < N:
                    disjoint_set.union(root + 2, (root+4) + 1)
                if col-1 >= 0:
                    disjoint_set.union(root + 1, (root-4) + 2)

        return disjoint_set.components

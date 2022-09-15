from typing import List


class DisjointSet:
    def __init__(self, row: int, col: int) -> None:
        self.rank = []
        self.parent = []
        self.count = 0
        for _ in range(row * col):
            self.rank.append(1)
            self.parent.append(-1)

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u: int, v: int) -> None:
        u_root, v_root = self.find(u), self.find(v)
        if u_root == v_root:
            return

        self.count -= 1
        if self.rank[u_root] >= self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[u_root] = v_root

    def set_parent(self, node: int) -> None:
        if self.parent[node] == -1:
            self.parent[node] = node
            self.count += 1

    def is_island(self, node: int) -> bool:
        return self.parent[node] >= 0

    def get_island_number(self) -> int:
        return self.count


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        output_list = []
        disjoint_set = DisjointSet(m, n)
        for x, y in positions:
            index = x * n + y
            island_neighbors = []
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor_index = (x+dx) * n + (y+dy)
                if not (0 <= x+dx < m and 0 <= y+dy < n):
                    continue

                if disjoint_set.is_island(neighbor_index):
                    island_neighbors.append(neighbor_index)

            disjoint_set.set_parent(index)
            for neighbor in island_neighbors:
                disjoint_set.union(index, neighbor)
            output_list.append(disjoint_set.get_island_number())

        return output_list

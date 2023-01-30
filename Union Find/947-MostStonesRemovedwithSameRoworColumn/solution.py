from collections import defaultdict
from typing import List


class DisjointSet:
    def __init__(self, num: int):
        self.set_num = num
        self.rank = [1] * num
        self.parent = [i for i in range(num)]

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u: int, v: int):
        u_root, v_root = self.find(u), self.find(v)

        if u_root == v_root:
            return

        self.set_num -= 1
        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        elif self.rank[u_root] == self.rank[v_root]:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        else:
            self.parent[u_root] = v_root


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        memo = defaultdict(list)
        disjoint_set = DisjointSet(n)

        for i, stone in enumerate(stones):
            row, col = f"row{stone[0]}", f"col{stone[1]}"
            if row in memo:
                node = memo[row][0]
                disjoint_set.union(node, i)
            if col in memo:
                node = memo[col][0]
                disjoint_set.union(node, i)

            memo[row].append(i)
            memo[col].append(i)

        irremovable_stones = disjoint_set.set_num
        return n - irremovable_stones

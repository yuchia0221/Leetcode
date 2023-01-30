from typing import List


class DisjointSet:
    def __init__(self, num: int):
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

        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        elif self.rank[u_root] == self.rank[v_root]:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        else:
            self.parent[u_root] = v_root


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        group_num = n
        disjoint_set = DisjointSet(n)

        for timestamp, person1, person2 in sorted(logs):
            if disjoint_set.find(person1) != disjoint_set.find(person2):
                disjoint_set.union(person1, person2)
                group_num -= 1
            if group_num == 1:
                return timestamp

        return -1

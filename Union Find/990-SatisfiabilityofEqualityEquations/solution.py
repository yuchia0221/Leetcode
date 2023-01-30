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
    def equationsPossible(self, equations: List[str]) -> bool:
        disjoint_set = DisjointSet(26)

        for variable1, relation, _, variable2 in equations:
            if relation == "=":
                node1, node2 = char_to_int(variable1), char_to_int(variable2)
                disjoint_set.union(node1, node2)

        for variable1, relation, _, variable2 in equations:
            if relation == "!":
                node1, node2 = char_to_int(variable1), char_to_int(variable2)
                if disjoint_set.find(node1) == disjoint_set.find(node2):
                    return False

        return True


def char_to_int(char: str) -> int:
    return ord(char)-97

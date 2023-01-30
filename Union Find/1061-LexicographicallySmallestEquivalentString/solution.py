class DisjointSet:
    def __init__(self, num: int):
        self.parent = [i for i in range(num)]

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u: int, v: int):
        u_root, v_root = self.find(u), self.find(v)

        if u_root == v_root:
            return

        if u_root < v_root:
            self.parent[v_root] = u_root
        else:
            self.parent[u_root] = v_root


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        disjoint_set = DisjointSet(26)

        for char1, char2 in zip(s1, s2):
            int1, int2 = char_to_int(char1), char_to_int(char2)
            disjoint_set.union(int1, int2)

        result = []
        for char in baseStr:
            char_ascii = disjoint_set.find(char_to_int(char))
            result.append(chr(char_ascii+97))

        return "".join(result)


def char_to_int(char: str) -> int:
    return ord(char)-97

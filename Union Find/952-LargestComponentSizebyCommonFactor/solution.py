from collections import defaultdict
from typing import List


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.size = [1] * (n+1)
        self.parent = [i for i in range(n+1)]

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u: int, v: int) -> None:
        u_root, v_root = self.find(u), self.find(v)
        if u_root == v_root:
            return

        if self.size[u_root] >= self.size[v_root]:
            self.size[u_root] += self.size[v_root]
            self.parent[v_root] = u_root
        else:
            self.size[v_root] += self.size[u_root]
            self.parent[u_root] = v_root


class Solution:
    def get_all_prime_factors(self, num: int) -> List[int]:
        factor = 2
        prime_factors = set()
        while num >= pow(factor, 2):
            if num % factor == 0:
                prime_factors.add(factor)
                num = num // factor
            else:
                factor += 1

        prime_factors.add(num)
        return list(prime_factors)

    def largestComponentSize(self, nums: List[int]) -> int:
        num_factor_map = {}
        disjoint_set = DisjointSet(max(nums))

        for num in nums:
            prime_factors = self.get_all_prime_factors(num)
            num_factor_map[num] = prime_factors[0]
            for i in range(0, len(prime_factors)-1):
                disjoint_set.union(prime_factors[i], prime_factors[i+1])

        max_size = 0
        group_count = defaultdict(int)
        for num in nums:
            group_id = disjoint_set.find(num_factor_map[num])
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id])

        return max_size

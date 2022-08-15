from collections import defaultdict
from typing import List


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.size = {i: 1 for i in range(n)}
        self.parent = {i: i for i in range(n)}

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            # Path Compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return

        # Union by Size
        if self.size[root_x] >= self.size[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]

    def find_max_size(self) -> int:
        return max(self.size.values())


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        memo = defaultdict(int)
        disjoint_set = DisjointSet(len(nums))
        for i in range(len(nums)):
            if nums[i] in memo:
                continue

            memo[nums[i]] = i

            if nums[i]+1 in memo:
                disjoint_set.union(i, memo[nums[i]+1])
            if nums[i]-1 in memo:
                disjoint_set.union(i,
                                   memo[nums[i]-1])

        return disjoint_set.find_max_size()

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.len_nums = len(nums)
        self.tree = [0] * self.len_nums + nums
        for i in range(self.len_nums - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        index = self.len_nums + index
        self.tree[index] = val
        while index > 1:
            self.tree[index // 2] = self.tree[index] + self.tree[(index - 1) if (index % 2) else (index + 1)]
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.len_nums
        right += self.len_nums
        res = 0
        while left <= right:
            if left % 2:
                res += self.tree[left]
                left += 1
            left //= 2

            if not (right % 2):
                res += self.tree[right]
                right -= 1
            right //= 2

        return res

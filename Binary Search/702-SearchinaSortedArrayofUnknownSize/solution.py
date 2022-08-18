from typing import List


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
    def get(self, index: int) -> int:
        ...


class Solution:
    def search(self, reader: ArrayReader, target: int) -> int:
        right = 1
        while reader.get(right) < target:
            right *= 2

        left = right // 2
        while left <= right:
            mid = left + (right-left) // 2
            value = reader.get(mid)
            if value == target:
                return mid
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

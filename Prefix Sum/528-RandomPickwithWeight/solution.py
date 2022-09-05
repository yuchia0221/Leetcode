from functools import lru_cache
from random import randint
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.weights = w
        for i in range(1, len(w)):
            self.weights[i] += self.weights[i-1]

    def pickIndex(self) -> int:
        random_number = randint(1, self.weights[-1])

        # return bisect.bisect_left(self.weights)
        return self.binary_search(random_number)

    @lru_cache
    def binary_search(self, number: int) -> int:
        left, right = 0, len(self.weights)
        while left < right:
            mid = (left+right) // 2
            if number <= self.weights[mid]:
                right = mid
            else:
                left = mid + 1

        return left

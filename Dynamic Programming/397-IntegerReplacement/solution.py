from functools import lru_cache


class Solution:
    @lru_cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if self.is_number_even(n):
            return self.integerReplacement(n // 2) + 1
        else:
            return min(self.integerReplacement(n-1), self.integerReplacement(n+1)) + 1

    def is_number_even(self, num):
        return num % 2 == 0

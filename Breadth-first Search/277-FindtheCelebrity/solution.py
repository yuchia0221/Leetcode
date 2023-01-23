from functools import cache


# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    ...


class Solution:
    @cache
    def cached_knows(self, a: int, b: int) -> bool:
        return knows(a, b)

    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if self.cached_knows(candidate, i):
                candidate = i

        if self.is_celebrity(candidate, n):
            return candidate
        return -1

    def is_celebrity(self, candidate: int, n: int) -> bool:
        for i in range(n):
            if i == candidate:
                continue
            if self.cached_knows(candidate, i) or not self.cached_knows(i, candidate):
                return False
        return True

from functools import cache


class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i == 0:
                return j
            if j == 0:
                return i

            if s1[i-1] == s2[j-1]:
                return dp(i-1, j-1)

            return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1

        return dp(len(s1), len(s2))

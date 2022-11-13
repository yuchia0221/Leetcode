from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dp(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return dp(l+1, r-1) + 2

            return max(dp(l, r-1), dp(l+1, r))

        n = len(s)
        return dp(0, n-1)

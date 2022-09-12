class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [i for i in range(n+1)]
        memo[n] = 0

        for i in range(2, n+1):
            for j in range(1, i):
                memo[i] = max(memo[i], memo[j] * memo[i-j])

        return memo[n]

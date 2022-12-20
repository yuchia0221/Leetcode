from functools import cache


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @cache
        def dp(d: int, target: int) -> int:
            if d == 0:
                return 0 if target > 0 else 1

            value = 0
            for k in range(max(0, target-f), target):
                value += dp(d-1, k)

            return value

        return dp(d, target) % (pow(10, 9) + 7)

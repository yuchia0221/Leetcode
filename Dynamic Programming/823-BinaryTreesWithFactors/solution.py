from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = [1] * len(arr)
        index = {number: i for i, number in enumerate(arr)}

        for i, number in enumerate(arr):
            for j in range(i):
                if number % arr[j] == 0:
                    right = number / arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]

        return sum(dp) % (pow(10, 9) + 7)

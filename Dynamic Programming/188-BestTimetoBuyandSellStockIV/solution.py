from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        max_profit = [0] * (k+1)
        min_cost = [float("inf")] * (k+1)

        for price in prices:
            for i in range(1, k+1):
                min_cost[i] = min(min_cost[i], price-max_profit[i-1])
                max_profit[i] = max(max_profit[i], price-min_cost[i])

        return max_profit[k]

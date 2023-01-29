from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_sell = t2_sell = 0
        t1_hold = t2_hold = float("-inf")

        for price in prices:
            t2_sell = max(t2_sell, t2_hold+price)
            t2_hold = max(t2_hold, t1_sell-price)
            t1_sell = max(t1_sell, t1_hold+price)
            t1_hold = max(t1_hold, -price)

        return t2_sell

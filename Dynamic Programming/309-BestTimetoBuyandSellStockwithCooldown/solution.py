from typing import List


class Solution:
    def maxProfit(self, prices: List[int]):
        sold, held, reset = float("-inf"), float("-inf"), 0
        for price in prices:
            held, reset, sold = max(held, reset-price), max(reset, sold), held+price

        return max(sold, reset)

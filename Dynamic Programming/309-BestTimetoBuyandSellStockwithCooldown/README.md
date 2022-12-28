# Best Time to Buy and Sell Stock with Cooldown

Problem can be found in [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)!

### [Solution](/Dynamic%20Programming/309-BestTimetoBuyandSellStockwithCooldown/solution.py): Dynamic Programming

```python
def maxProfit(prices: List[int]):
    sold, held, reset = float("-inf"), float("-inf"), 0
    for price in prices:
        held, reset, sold = max(held, reset-price), max(reset, sold), held+price

    return max(sold, reset)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

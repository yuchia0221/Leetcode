# Best Time to Buy and Sell Stock III

Problem can be found in [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)!

### [Solution](/Dynamic%20Programming/123-BestTimetoBuyandSellStockIII/solution.py): Dynamic Programming

```python
def maxProfit(prices: List[int]) -> int:
    t1_sell = t2_sell = 0
    t1_hold = t2_hold = float("-inf")

    for price in prices:
        t2_sell = max(t2_sell, t2_hold+price)
        t2_hold = max(t2_hold, t1_sell-price)
        t1_sell = max(t1_sell, t1_hold+price)
        t1_hold = max(t1_hold, -price)

    return t2_sell
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

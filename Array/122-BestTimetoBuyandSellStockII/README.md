# Best Time to Buy and Sell Stock II

Problem can be found in [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)!

### [Solution](/Array/122-BestTimetoBuyandSellStockII/solution.py)

```python
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i]-prices[i-1] > 0:
            max_profit += prices[i]-prices[i-1]

    return max_profit
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

# Best Time to Buy and Sell Stock IV

Problem can be found in [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)!

### [Solution](/Dynamic%20Programming/188-BestTimetoBuyandSellStockIV/solution.py): Dynamic Programming

```python
def maxProfit(k: int, prices: List[int]) -> int:
    max_profit = [0] * (k+1)
    min_cost = [float("inf")] * (k+1)

    for price in prices:
        for i in range(1, k+1):
            min_cost[i] = min(min_cost[i], price-max_profit[i-1])
            max_profit[i] = max(max_profit[i], price-min_cost[i])

    return max_profit[k]
```

Time Complexity: ![O(nk)](<https://latex.codecogs.com/svg.image?\inline&space;O(nk)>), Space Complexity: ![O(k)](<https://latex.codecogs.com/svg.image?\inline&space;O(k)>)

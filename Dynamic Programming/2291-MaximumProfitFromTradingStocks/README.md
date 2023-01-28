# Maximum Profit From Trading Stocks

Problem can be found in [here](https://leetcode.com/problems/maximum-profit-from-trading-stocks/)!

### [Solution](/Dynamic%20Programming/2291-MaximumProfitFromTradingStocks/solution.py): Dynamic Programming

```python
def maximumProfit(present: List[int], future: List[int], budget: int) -> int:
    @cache
    def dfs(item: int, budget: int) -> int:
        if item == n or stock[item][0] > budget:
            return 0

        price, item_profit = stock[item]
        buy_item = item_profit + dfs(item+1, budget-price)
        skip_item = dfs(item+1, budget)

        return max(buy_item, skip_item)

    stock = [[present[i], future[i]-present[i]]
                for i in range(len(present)) if future[i]-present[i] > 0 and future[i] > present[i]]
    stock.sort()
    n = len(stock)
    return dfs(0, budget)
```

Time Complexity: ![O(nb+nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nb+nlogn)>), Space Complexity: ![O(nb)](<https://latex.codecogs.com/svg.image?\inline&space;O(nb)>), where n is the number of items and b is the value of budget.

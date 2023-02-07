# Stock Price Fluctuation

Problem can be found in [here](https://leetcode.com/problems/stock-price-fluctuation/)!

### [Solution](/Design/2034-StockPriceFluctuation/solution.py)

```python
class StockPrice:
    def __init__(self):
        self.latest_time = 0
        self.max_heap = []
        self.min_heap = []
        self.time_price_map = dict()

    def update(self, timestamp: int, price: int) -> None:
        self.time_price_map[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)
        
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))
        

    def current(self) -> int:
        return self.time_price_map[self.latest_time]

    def maximum(self) -> int:
        price, time = self.max_heap[0]
        
        while -price != self.time_price_map[time]:
            heappop(self.max_heap)
            price, time = self.max_heap[0]
            
        return -price

    def minimum(self) -> int:
        price, time = self.min_heap[0]
        
        while price != self.time_price_map[time]:
            heappop(self.min_heap)
            price, time = self.min_heap[0]
            
        return price
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

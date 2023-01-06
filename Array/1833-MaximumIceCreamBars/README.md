# Maximum Ice Cream Bars

Problem can be found in [here](https://leetcode.com/problems/maximum-ice-cream-bars/)!

### [Solution](/Array/1833-MaximumIceCreamBars/solution.py): Sorting + Greedy

```python
def maxIceCream(costs: List[int], coins: int) -> int:
    index = 0
    costs.sort()

    while coins >= 0 and index < len(costs):
        if costs[index] <= coins:
            coins -= costs[index]
            index += 1
        else:
            break

    return index
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

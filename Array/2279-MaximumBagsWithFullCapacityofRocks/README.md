# Maximum Bags With Full Capacity of Rocks

Problem can be found in [here](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/)!

### [Solution](/Array/2279-MaximumBagsWithFullCapacityofRocks/solution.py): Sorting + Greedy

```python
def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    remainings = sorted(map(lambda x, y: x-y, capacity, rocks))

    full_bags_num = 0
    for remain in remainings:
        if remain <= additionalRocks:
            additionalRocks -= remain
            full_bags_num += 1
        else:
            break

    return full_bags_num
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

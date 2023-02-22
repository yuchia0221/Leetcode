# Capacity To Ship Packages Within D Days

Problem can be found in [here](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)!

### [Solution](/Binary%20Search/1011-CapacityToShipPackagesWithinDDays/solution.py): Binary Search

```python
def shipWithinDays(weights: List[int], days: int) -> int:
    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        current_weight, ship_days = 0, 1
        for weight in weights:
            if current_weight + weight > mid:
                current_weight = 0
                ship_days += 1
            current_weight += weight

        if ship_days > days:
            left = mid + 1
        else:
            right = mid

    return left
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

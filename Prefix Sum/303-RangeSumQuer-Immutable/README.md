# Range Sum Query - Immutable

Problem can be found in [here](https://leetcode.com/problems/range-sum-query-immutable/)!

### [Solution](/Prefix%20Sum/238-ProductofArrayExceptSelf/solution.py): Prefix Sum

```python
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0, nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[i]+nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]
```

Explanation: Instead of calculating the range sum of an array every time, we can precompute the value and store it in the new array prefix_sum (prefix_sum[i] stores the sum from 0 to i). To compute the sum range from left to right, we can simply return prefix_sum[right] - prefix_sum[left]. There is only one edge case to solve: when left=0, we should only return prefix_sum[right] since it already stores the sum from 0 to right.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

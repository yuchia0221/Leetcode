# Minimum Average Difference

Problem can be found in [here](https://leetcode.com/problems/minimum-average-difference/)!

### [Solution](/Prefix%20Sum/2256-MinimumAverageDifference/solution.py): Prefix Sum

```python
def minimumAverageDifference(nums: List[int]) -> int:
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]

    min_index, min_difference = 0, float("inf")
    for i in range(n):
        left_part_average = int(prefix_sum[i] / (i+1))
        if i == n-1:
            right_part_average = 0
        else:
            right_part_average = int((prefix_sum[-1]-prefix_sum[i]) / (n-i-1))

        current_difference = abs(left_part_average-right_part_average)
        if current_difference < min_difference:
            min_index = i
            min_difference = current_difference

    return min_index
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

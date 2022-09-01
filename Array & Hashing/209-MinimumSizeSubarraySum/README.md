# Minimum Size Subarray Sum

Problem can be found in [here](https://leetcode.com/problems/minimum-size-subarray-sum/)!

### [Solution](/Array%20%26%20Hashing/209-MinimumSizeSubarraySum/solution.py): Two pointers

```python
def minSubArrayLen(target: int, nums: List[int]) -> int:
    current_sum = slow = 0
    minimum_size = float("inf")
    for index, num in enumerate(nums):
        current_sum += num
        while current_sum >= target:
            if current_sum == target:
                minimum_size = min(minimum_size, index-slow+1)
            current_sum -= nums[slow]
            slow += 1

    return minimum_size if minimum_size != float("inf") else 0
```

Explanation: In each iteration, we increase the size of the sliding window. If current sum is greater or equal to the target value. We can safely increment since the minimum subarray starting with this index with sum≥*s* has been achieved. We only need to check for if the target value equals the current value.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

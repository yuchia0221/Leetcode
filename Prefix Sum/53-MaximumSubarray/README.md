# Maximum Subarray

Problem can be found in [here](https://leetcode.com/problems/maximum-subarray/)!

### [Solution](/Prefix%20Sum/53-MaximumSubarray/solution.py): Prefix Sum

```python
def maxSubArray(nums: List[int]) -> int:
    current_sum = max_sum = 0
    for num in nums:
        current_sum = max(current_sum+num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```

Explanation: Define the maximum value of a given subarray from index 0 to i as P(i) and the original array as nums. We can easily write down the recursion function P(i) = max(nums[i], P(i-1)+nums[i]).

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

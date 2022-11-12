# Burst Balloons

Problem can be found in [here](https://leetcode.com/problems/burst-balloons/)!

### [Solution](/Dynamic%20Programming/312-BurstBalloons/solution.py): Dynamic Programming

```python
def maxCoins(nums: List[int]) -> int:
    @cache
    def dp(left, right):
        if right - left < 0:
            return 0

        result = 0
        for i in range(left, right + 1):
            gain = nums[left - 1] * nums[i] * nums[right + 1]
            remaining = dp(left, i - 1) + dp(i + 1, right)
            result = max(result, remaining + gain)
        return result

    nums = [1] + nums + [1]
    return dp(1, len(nums) - 2)
```

Time Complexity: ![O(n^3)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^3)>), Space Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>)

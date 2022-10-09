# Target Sum

Problem can be found in [here](https://leetcode.com/problems/target-sum/)!

### [Solution](/Backtracking/494-TargetSum/solution.py): Backtracking

```python
def findTargetSumWays(nums: List[int], target: int) -> int:
    @cache
    def helper(index: int, current_sum: int) -> int:
        if index == len(nums):
            return int(current_sum == target)

        return helper(index+1, current_sum+nums[index]) + helper(index+1, current_sum-nums[index])

    return helper(0, 0)
```

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), where n is the length of nums and m is sum of nums.

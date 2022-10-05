# Subsets

Problem can be found in [here](https://leetcode.com/problems/subsets/)!

### [Solution](/Backtracking/78-Subsets/solution.py): Backtracking

```python
def subsets(nums: List[int]) -> List[List[int]]:
    def helper(tempt: List[int], index: int):
        if len(tempt) <= len(nums):
            result.append(tempt)

        for i in range(index, len(nums)):
            helper(tempt+[nums[i]], i+1)

    result = []
    helper([], 0)
    return result
```

Explanation: We can apply depth-first search to solve this problem. The key to avoid duplicated solutions is to pass in a variable index in each iteration of dfs.

Time Complexity: ![O(n*2^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n2^n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of nums.
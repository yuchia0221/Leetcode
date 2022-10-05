# Subsets II

Problem can be found in [here](https://leetcode.com/problems/subsets-ii/)!

### [Solution](/Backtracking/90-SubsetsII/solution.py): Backtracking

```python
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    def helper(tempt: List[int], index: int):
        result.append(tempt)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            helper(tempt+[nums[i]], i+1)

    result = []
    nums.sort()
    helper([], 0)
    return result
```

Time Complexity: ![O(n*2^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n*2^n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of nums.

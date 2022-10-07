# Increasing Subsequences

Problem can be found in [here](https://leetcode.com/problems/increasing-subsequences/)!

### [Solution](/Backtracking/491-IncreasingSubsequences/solution.py): Backtracking

```python
def findSubsequences(nums: List[int]) -> List[List[int]]:
    def helper(tempt: List[int], index: int):
        if len(tempt) > 1:
            result.append(tempt)

        visited = set()
        for i in range(index, len(nums)):
            if tempt and tempt[-1] > nums[i] or nums[i] in visited:
                continue
            visited.add(nums[i])
            helper(tempt+[nums[i]], i+1)

    result = []
    helper([], 0)
    return list(result)
```

Explanation: Use the backtrack algorithm to solve this problem. In each iteration, if current value is bigger than the previous element we append into the tempt list, we can continue to append it into the tempt list.  

Time Complexity: ![O(2^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(2^n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of the nums array.

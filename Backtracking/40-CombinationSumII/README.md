# Combination Sum II

Problem can be found in [here](https://leetcode.com/problems/combination-sum-ii/)!

### [Solution](/Backtracking/40-CombinationSumII/solution.py): Depth-first Search

```python
def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    output_list = []
    candidates = sorted(candidates)
    dfs(candidates, 0, target, [], output_list)
    return output_list

def dfs(nums: List[int], index: int, target: int, tempt: List[int], answer: List[List[int]]) -> None:
    if target < 0:
        return
    elif target == 0:
        answer.append(list(tempt))
        return

    for i in range(index, len(nums)):
        if i > index and nums[i-1] == nums[i]:
            continue
        else:
            tempt.append(nums[i])
            dfs(nums, i+1, target-nums[i], tempt, answer)
            tempt.pop()
```

Explanation: We can apply depth-first search to solve this problem. The key to avoid duplicated solutions is to pass in a variable index in each iteration of dfs.

Time Complexity: ![O(n^k)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^k)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of candidates and k is the value of target divided by the minimum value in candidates.

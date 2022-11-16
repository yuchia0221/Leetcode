# Jump Game II

Problem can be found in [here](https://leetcode.com/problems/jump-game-ii/)!

### [Solution](/Array/45-JumpGameII/solution.py): Greedy

```python
def jump(nums: List[int]) -> int:
    start = end = step = 0
    while end < len(nums) - 1:
        step += 1
        start, end = end+1, max(i+nums[i] for i in range(start, end+1))

    return step
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

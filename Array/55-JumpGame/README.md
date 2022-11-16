# Jump Game

Problem can be found in [here](https://leetcode.com/problems/jump-game/)!

### [Solution](/Array/55-JumpGame/solution.py): Greedy

```python
def canJump(nums: List[int]) -> bool:
    last_position = len(nums)-1
    for index in range(len(nums)-1, -1, -1):
        if index + nums[index] >= last_position:
            last_position = index

    return last_position == 0
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

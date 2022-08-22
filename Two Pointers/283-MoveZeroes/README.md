# Move Zeroes

Problem can be found in [here](https://leetcode.com/problems/move-zeroes/)!

### [Solution](//Multiple%20Pointers/283-MoveZeroes//solution.py)

```python
def moveZeroes(nums: List[int]) -> None:
      slow = fast = 0
      while fast < len(nums):
          if nums[fast] != 0:
              nums[slow], nums[fast] = nums[fast], nums[slow]
              slow += 1
          fast += 1
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

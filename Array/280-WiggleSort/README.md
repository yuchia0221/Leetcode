# Wiggle Sort

Problem can be found in [here](https://leetcode.com/problems/wiggle-sort/)!

### [Solution](/Array/280-WiggleSort/solution.py)

```python
def wiggleSort(nums: List[int]) -> None:
    for i in range(len(nums)-1):
        if (i % 2 == 0 and nums[i] > nums[i+1]) or (i % 2 == 1 and nums[i] < nums[i+1]):
            nums[i], nums[i+1] = nums[i+1], nums[i]
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

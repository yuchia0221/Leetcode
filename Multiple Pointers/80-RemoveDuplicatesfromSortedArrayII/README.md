# Remove Duplicates from Sorted Array II

Problem can be found in [here](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)!

### [Solution](//Multiple%20Pointers/912-SortanArray/solution.py)

```python
def removeDuplicates(nums: List[int]) -> int:
    if len(nums) < 3:
        return len(nums)

    slow = fast = 2
    while fast <= len(nums)-1:
        if nums[fast] != nums[slow-2]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    
    return slow
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

# Remove Duplicates from Sorted Array

Problem can be found in [here](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)!

### [Solution](//Multiple%20Pointers/26-RemoveDuplicatesfromSortedArray/solution.py)

```python
def removeDuplicates(nums: List[int]) -> int:
    slow, fast = 0, 1
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1

    return slow + 1
```

Explanation: We use a fast pointer to find the next unique value. Then, we switch the value between slow+1 and fast.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

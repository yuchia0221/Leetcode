# Single Element in a Sorted Array

Problem can be found in [here](https://leetcode.com/problems/single-element-in-a-sorted-array/)!

### [Solution](/Binary%20Search/540-SingleElementinaSortedArray/solution.py): Binary Search

```python
def singleNonDuplicate(nums: List[int]) -> int:
    left, right = 0, len(nums)-1

    while left < right:
        mid = (left+right) // 2
        is_first_half_even = (mid-left+1) % 2 == 0
        if nums[mid] == nums[mid+1]:
            if is_first_half_even:
                right = mid - 1
            else:
                left = mid + 2
        elif nums[mid-1] == nums[mid]:
            if is_first_half_even:
                left = mid + 1
            else:
                right = mid - 2
        else:
            return nums[mid]

    return nums[left]
```

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

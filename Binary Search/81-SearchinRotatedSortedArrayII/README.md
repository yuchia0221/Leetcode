# Search in Rotated Sorted Array II

Problem can be found in [here](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)!

### [Solution](/Binary%20Search/81-SearchinRotatedSortedArrayII/solution.py): Binary Search

```python
def search(nums: List[int], target: int) -> bool:
    left, right = 0, len(nums)-1

    while left <= right:
        while left < right and nums[left] == nums[left+1]:
            left += 1
        while left < right and nums[right] == nums[right-1]:
            right -= 1

        mid = (right+left) // 2
        if nums[mid] == target:
            return True

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False
```

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

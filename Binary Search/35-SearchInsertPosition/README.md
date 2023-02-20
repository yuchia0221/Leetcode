# Search Insert Position

Problem can be found in [here](https://leetcode.com/problems/search-insert-position/)!

### [Solution](/Binary%20Search/35-SearchInsertPosition/solution.py): Binary Search

```python
def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left
```

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

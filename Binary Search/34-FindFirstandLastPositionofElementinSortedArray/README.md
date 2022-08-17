# Find First and Last Position of Element in Sorted Array

Problem can be found in [here](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)!

### [Solution](/Binary%20Search/34-FindFirstandLastPositionofElementinSortedArray/solution.py): Binary Search

```python
def searchRange(nums: List[int], target: int) -> List[int]:
    def binary_search_first():
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def binary_search_last():
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left = binary_search_first()
    right = binary_search_last()
    return [left, right] if left <= right else [-1, -1]
```

Explanation: The key to solve this problem is to perform binary search twice. One searches for the first element of the target value. The other searches for the last element of the target value.

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

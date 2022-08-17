# Binary Search

Problem can be found in [here](https://leetcode.com/problems/binary-search/)!

### [Solution](/Binary%20Search/704-BinarySearch/solution.py): Binary Search

```python
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1
```

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

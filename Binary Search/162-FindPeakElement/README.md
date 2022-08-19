# Find Peak Element

Problem can be found in [here](https://leetcode.com/problems/find-peak-element/)!

### [Solution](/Binary%20Search/162-FindPeakElement/solution.py): Binary Search

```python
def findPeakElement(nums: List[int]) -> int:
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left+right) // 2
        if nums[mid] >= nums[mid+1]:
            right = mid
        else:
            left = mid + 1

    return left
```

Explanation: We can slightly modify binary search to find the peak element. Note that returning any correct peak element will be accepted. In each iteration, we keep track the relationship between `array[mid]` and `array[mid+1]`, where mid is the average of the left and right pointer.

-   If array[mid] ≥ array[mid+1]: there must be at least one peak element from [left, mid]
-   If array[mid < array[mid+1]: there may be a peak from [left, mid], but there must be at least one peak from [mid+1, right]

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

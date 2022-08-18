# Search in a Sorted Array of Unknown Size

Problem can be found in [here](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/)!

### [Solution](/Binary%20Search/702-SearchinaSortedArrayofUnknownSize/solution.py): Binary Search

```python
def search(reader: ArrayReader, target: int) -> int:
    right = 1
    while reader.get(right) < target:
        right *= 2

    left = right // 2
    while left <= right:
        mid = left + (right-left) // 2
        value = reader.get(mid)
        if value == target:
            return mid
        elif value > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1
```

Explanation: The only difference between this problem and typical binary search problem is that this problem does not provide the length for the array, which seems to make performing binary search impossible. However, we can first find the boundary of the array and target (if there is one) in $O(logn)$ time. Since we know the boundary, we can perform the typical binary search we used to.

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

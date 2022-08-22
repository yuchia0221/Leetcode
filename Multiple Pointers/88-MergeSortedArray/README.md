# Merge Sorted Array

Problem can be found in [here](https://leetcode.com/problems/merge-sorted-array/)!

### [Solution](//Multiple%20Pointers/88-MergeSortedArray/solution.py)

```python
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j = m-1, n-1
    index = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] >= nums2[j]:
            nums1[index] = nums1[i]
            i -= 1
        else:
            nums1[index] = nums2[j]
            j -= 1
        index -= 1
```

Time Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+m)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

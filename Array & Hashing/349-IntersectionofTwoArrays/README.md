# Intersection of Two Arrays

Problem can be found in [here](https://leetcode.com/problems/intersection-of-two-arrays/)!

### [Solution](/Array%20%26%20Hashing/349-IntersectionofTwoArrays/solution.py): Hash Table

```python
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_set, nums2_set = set(nums1), set(nums2)
    return list(nums1_set & nums2_set)
```

Explanation: We can use set operation to solve this problem. Just find the intersection of two arrays.

Time Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+m)>), Space Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+m)>), where n and m is the length of nums1 and nums2, respectively.

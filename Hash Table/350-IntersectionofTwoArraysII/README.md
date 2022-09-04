# Intersection of Two Arrays II

Problem can be found in [here](https://leetcode.com/problems/intersection-of-two-arrays-ii/)!

### [Solution](/Hash%20Table/350-IntersectionofTwoArraysII/solution.py): Hash Table

```python
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    memo = defaultdict(int)
    for num in nums1:
        memo[num] += 1

    output_list = []
    for num in nums2:
        if memo[num] > 0:
            output_list.append(num)
            memo[num] -= 1

    return output_list
```

Explanation: Instead of using two sets to solve this problem as [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/), we can use a hash table or dictionary in Python to store the maximum number of occurrences for each character. Therefore, the returned value will appear as many times as it shows in both arrays.

Time Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+m)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n and m is the length of nums1 and nums2, respectively.

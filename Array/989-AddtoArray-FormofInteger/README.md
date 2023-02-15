# Add to Array-Form of Integer

Problem can be found in [here](https://leetcode.com/problems/add-to-array-form-of-integer/)!

### [Solution](/Array/989-AddtoArray-FormofInteger//solution.py)

```python
def addToArrayForm(nums: List[int], k: int) -> List[int]:
    for i in range(len(nums)-1, -1, -1):
        k, nums[i] = divmod(nums[i]+k, 10)

    return [int(i) for i in str(k)] + nums if k else nums
```

Time Complexity: ![O(max(n, logk))](<https://latex.codecogs.com/svg.image?%5Cinline&space;O(max(n,%20logk))>), Space Complexity: ![O(max(n, logk))](<https://latex.codecogs.com/svg.image?%5Cinline&space;O(max(n,%20logk))>), where n is the length of array nums.

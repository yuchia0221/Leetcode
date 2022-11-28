# Next Permutation

Problem can be found in [here](https://leetcode.com/problems/next-permutation/)!

### [Solution](/Two%20Pointers/31-NextPermutation/solution.py): Two pointers

```python
def nextPermutation(nums: List[int]) -> None:
    last_peak_index = len(nums)-1
    while last_peak_index > 0 and nums[last_peak_index] <= nums[last_peak_index-1]:
        last_peak_index -= 1

    if last_peak_index == 0:
        nums.reverse()
        return

    i, j = last_peak_index - 1, len(nums)-1
    while nums[j] <= nums[i]:
        j -= 1

    nums[i], nums[j] = nums[j], nums[i]
    left, right = i+1, len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

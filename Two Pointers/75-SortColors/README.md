# Sort Colors

Problem can be found in [here](https://leetcode.com/problems/sort-colors/)!

### [Solution](//Multiple%20Pointers/75-SortColors/solution.py): Multiple Pointers

```python
def sortColors(nums: List[int]) -> None:
      red, current, blue = 0, 0, len(nums)-1
      while current <= blue:
          if nums[current] == 0:
              nums[red], nums[current] = nums[current], nums[red]
              red += 1
              current += 1
          elif nums[current] == 1:
              current += 1
          else:
              nums[current], nums[blue] = nums[blue], nums[current]
              blue -= 1
```

Explanation: Use three pointers to perform in-place sorting. If nums[mid] is 0, meaning that we need to swap the value in nums[left] and nums[mid] to make the array sorted. Another case is that if we encounter 2 in nums[mid], we know that we should swap nusmms[right] and nums[mid] to keep the array sorted. By doing so, the array will be sorted in O(n) time after iterating the whole array (worst case).

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

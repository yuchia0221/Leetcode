# Longest Mountain in Array

Problem can be found in [here](https://leetcode.com/problems/longest-mountain-in-array/)!

### [Solution](/Two%20Pointers/845-LongestMountaininArray/solution.py): Two Pointers

```python
def longestMountain(arr: List[int]) -> int:
    max_length, peak = 0, 1
    while peak < len(arr)-1:
        if arr[peak] > arr[peak-1] and arr[peak] > arr[peak+1]:
            left, right = peak-1, peak+1
            while left > 0 and arr[left] > arr[left-1]:
                left -= 1
            while right < len(arr)-1 and arr[right] > arr[right+1]:
                right += 1
            max_length = max(max_length, right-left+1)
            peak = right + 1
        else:
            peak += 1

    return max_length
```

Explanation: First, we can iterate through arr to find the peak element such that arr[peak-1] < arr[peak] < arr[peak+1]. After we find that, we can use two while loops to find the boundaries [i, j] (i ≤ j) of the mountain of both sides. If we find a peak, then we only need to search another peak starting from j + 1 instead of peak + 1.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

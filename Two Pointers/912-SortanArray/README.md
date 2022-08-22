# Sort an Array

Problem can be found in [here](https://leetcode.com/problems/sort-an-array/)!

### [Solution](//Multiple%20Pointers/912-SortanArray/solution.py)

```python
def sortArray(nums: List[int]) -> List[int]:
    def merge(start: int, mid: int, end: int) -> None:
        left_array = [nums[i] for i in range(start, mid+1)]
        right_array = [nums[i] for i in range(mid+1, end+1)]

        index = start
        left = right = 0
        n, m = mid-start+1, end-mid
        while left < n and right < m:
            if left_array[left] <= right_array[right]:
                nums[index] = left_array[left]
                left += 1
            else:
                nums[index] = right_array[right]
                right += 1
            index += 1

        while left < len(left_array):
            nums[index] = left_array[left]
            left += 1
            index += 1

        while right < len(right_array):
            nums[index] = right_array[right]
            right += 1
            index += 1

    def merge_sort(start: int, end: int) -> None:
        if start < end:
            mid = (start+end) // 2
            merge_sort(start, mid)
            merge_sort(mid+1, end)
            merge(start, mid, end)

    merge_sort(0, len(nums)-1)
    return nums
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

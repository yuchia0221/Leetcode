# Kth Largest Element in an Array

Problem can be found in [here](https://leetcode.com/problems/kth-largest-element-in-an-array/)!

### [Solution](/Array%20%26%20Hashing/215-KthLargestElementinanArray/solution.py): Quick Select

```python
def findKthLargest(nums: List[int], k: int) -> int:
    def quick_select(left: int, right: int):
        pivot_value, index = nums[right], left
        for i in range(left, right):
            if nums[i] <= pivot_value:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1

        nums[index], nums[right] = nums[right], nums[index]
        if index == k:
            return nums[index]
        elif index > k:
            return quick_select(left, index-1)
        else:
            return quick_select(index+1, right)

    k = len(nums)-k
    return quick_select(0, len(nums)-1)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>)

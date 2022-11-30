# Find the Kth Largest Integer in the Array

Problem can be found in [here](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/)!

### [Solution](/Array/1985-FindtheKthLargestIntegerintheArray/solution.py): Quick Select

```python
def kthLargestNumber(nums: List[str], k: int) -> str:
    def parition(left: int, right: int) -> int:
        pivot = nums[right]
        j = left

        for i in range(left, right):
            if int(nums[i]) <= int(pivot):
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        nums[j], nums[right] = nums[right], nums[j]
        return j

    def quick_select(left: int, right: int, k: int) -> str:
        if left == right:
            return nums[left]

        index = parition(left, right)
        if index == k:
            return nums[index]
        elif index > k:
            return quick_select(left, index-1, k)
        else:
            return quick_select(index+1, right, k)

    return quick_select(0, len(nums)-1, len(nums)-k)
```

Time Complexity: Average ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>) Wrost ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

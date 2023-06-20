# K Radius Subarray Averages

Problem can be found in [here](https://leetcode.com/problems/k-radius-subarray-averages/)!

### [Solution](/Sliding%20Window/2090-KRadiusSubarrayAverages/solution.py)

```python
def getAverages(nums: List[int], k: int) -> List[int]:
    if k == 0:
        return nums

    average_list = [-1] * len(nums)
    if len(nums) < 2*k + 1:
        return average_list

    current_sum = sum(nums[:2*k + 1])
    numbers_in_radius = 2*k + 1
    average_list[k] = current_sum // numbers_in_radius

    for i in range(numbers_in_radius, len(nums)):
        current_sum += nums[i] - nums[i-numbers_in_radius]
        average_list[i-k] = current_sum // numbers_in_radius

    return average_list
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

# Make Array Strictly Increasing

Problem can be found in [here](https://leetcode.com/problems/make-array-strictly-increasing/)!

### [Solution](/Dynamic%20Programming/1187-MakeArrayStrictlyIncreasing/solution.py): Dynamic Programming

```python
def makeArrayIncreasing(arr1: List[int], arr2: List[int]) -> int:
    @cache
    def get_minimum_operations(index: int, previous_value: int) -> int:
        if index == len(arr1):
            return 0

        current_cost = float("inf")
        if arr1[index] > previous_value:
            current_cost = get_minimum_operations(index+1, arr1[index])

        new_index = bisect_right(arr2, previous_value)
        if new_index < len(arr2):
            current_cost = min(current_cost, 1 + get_minimum_operations(index+1, arr2[new_index]))

        return current_cost

    arr2.sort()
    minimum_operations = get_minimum_operations(0, -1)
    return minimum_operations if minimum_operations != float("inf") else -1
```

Time Complexity: ![O(mnlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(mnlogn)>), Space Complexity: ![O(mn)](<https://latex.codecogs.com/svg.image?\inline&space;O(mn)>), where m is the length of arr1 array and n is the length of arr2 array.

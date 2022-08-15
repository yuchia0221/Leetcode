# Two Sum II - Input Array Is Sorted

Problem can be found in [here](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)!

### [Solution](/Two%20Pointers/125-ValidPalindrome/solution.py): Two Pointers

```python
def twoSum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers)-1

    while left < right:
        current_value = numbers[left] + numbers[right]
        if current_value == target:
            break
        elif current_value < target:
            left += 1
        else:
            right -= 1

    return [left+1, right+1]
```

Explanation: Using the infomation that array is already sorted in descending order, we can keep moving left and right pointers until we reach the unique solution. If we combine the value of the leftmost and the rightmost element, there might be three cases.

1. Left + Right = target: we find the solution
2. Left + Right < target: we need to move the left pointer to right as this will make the value larger
3. Left + Right > target: we need to move the right pointer to left as this will make the value smaller

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

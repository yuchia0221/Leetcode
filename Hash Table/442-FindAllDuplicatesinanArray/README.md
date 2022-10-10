# Find All Duplicates in an Array

Problem can be found in [here](https://leetcode.com/problems/find-all-duplicates-in-an-array/)!

### [Solution](/Hash%20Table//986-IntervalListIntersections/solution.py): Hash Table

```python
def findDuplicates(nums: List[int]) -> List[int]:
    output_list = []
    for num in nums:
        abs_num = abs(num)
        if nums[abs_num-1] < 0:
            output_list.append(abs_num)
        else:
            nums[abs_num-1] = -nums[abs_num-1]

    return output_list
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

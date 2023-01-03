# Delete Columns to Make Sorted

Problem can be found in [here](https://leetcode.com/problems/delete-columns-to-make-sorted/)!

### [Solution](/Array/944-DeleteColumnstoMakeSorted/solution.py)

```python
def minDeletionSize(strs: List[str]) -> int:
    deleted_columns = 0

    for column in zip(*strs):
        for i in range(1, len(column)):
            if column[i-1] > column[i]:
                deleted_columns += 1
                break

    return deleted_columns
```

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n is the length of array strs and m is the length of an element in the array.

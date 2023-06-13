# Equal Row and Column Pairs

Problem can be found in [here](https://leetcode.com/problems/equal-row-and-column-pairs/)!

### [Solution](/Hash%20Table/2352-EqualRowandColumnPairs/solution.py): Hash Table

```python
def equalPairs(grid: List[List[int]]) -> int:
    memo = defaultdict(int)
    for row in grid:
        memo[tuple(row)] += 1

    equal_pairs = 0
    for col in zip(*grid):
        equal_pairs += memo[tuple(col)]

    return equal_pairs
```

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), where n is the number of rows and m is the number of columns.

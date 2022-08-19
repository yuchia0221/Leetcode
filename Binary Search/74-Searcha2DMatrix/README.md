# 74. Search a 2D Matrix

Problem can be found in [here](https://leetcode.com/problems/search-a-2d-matrix/)!

### [Solution](/Binary%20Search/74-Searcha2DMatrix/solution.py): Binary Search

```python
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row, column = len(matrix), len(matrix[0])
    left, right = 0, row*column - 1
    while left <= right:
        mid = (left+right) // 2
        row_number, column_number = mid // column, mid % column
        candidate = matrix[row_number][column_number]
        if candidate == target:
            return True
        elif candidate > target:
            right = mid - 1
        else:
            left = mid + 1

    return False
```

Explanation: We can simply convert this problem to typical binary search question by viewing the matrix as a sorted 1-d array. By doing so, we can perform binary search to find the target.

Time Complexity: ![O(lognm)](<https://latex.codecogs.com/svg.image?\inline&space;O(lognm)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

# As Far from Land as Possible

Problem can be found in [here](https://leetcode.com/problems/as-far-from-land-as-possible/)!

### [Solution](/Breadth-first%20Search/1162-AsFarfromLandasPossible/solution.py): Breadth-first Search

```python
def maxDistance(grid: List[List[int]]) -> int:
    row_num, col_num = len(grid), len(grid[0])
    water_areas = []
    for row in range(row_num):
        for col in range(col_num):
            if grid[row][col] == 1:
                water_areas.append((row, col))

    if len(water_areas) == 0 or len(water_areas) == row_num*col_num:
        return -1

    queue = deque(water_areas)
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    max_distance = 0
    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            for dx, dy in directions:
                new_row, new_col = row+dx, col+dy
                if 0 <= new_row < row_num and 0 <= new_col < col_num and grid[new_row][new_col] == 0:
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = 1

        max_distance += 1

    return max_distance-1
```

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?O(nm)>), Space Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), where n and m are the number of row and column, respectively.

# Minimum Number of Arrows to Burst Balloons

Problem can be found in [here](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)!

### [Solution](/Array/452-MinimumNumberofArrowstoBurstBalloons/solution.py): Sorting + Greedy

```python
def findMinArrowShots(points: List[List[int]]) -> int:
    if not points:
        return 0

    points.sort(key=lambda x: x[1])
    arrows, previous = 1, points[0][1]

    for start, end in points:
        if previous < start:
            arrows += 1
            previous = end

    return arrows
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

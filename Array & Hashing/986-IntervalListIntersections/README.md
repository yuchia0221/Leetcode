# Interval List Intersections

Problem can be found in [here](https://leetcode.com/problems/interval-list-intersections/)!

### [Solution](/Array%20%26%20Hashing/986-IntervalListIntersections/solution.py): Two pointers

```python
def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i = j = 0
    output_list = []
    while i < len(firstList) and j < len(secondList):
        intersect_start_time = max(firstList[i][0], secondList[j][0])
        intersect_end_time = min(firstList[i][1], secondList[j][1])

        if intersect_start_time <= intersect_end_time:
            output_list.append([intersect_start_time, intersect_end_time])

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return output_list
```

Explanation: To determine whether `firstList[i]` and `secondList[j]` intersect, we can simply check the relation between `a=max(firstList[i].start, secondList[j].start)` and `b=min(firstList[i].end, secondList[j].end)`. If a ≤ b, meaning that there is an intersection. Otherwise, there is no intersection between two intervals. We can tell the next step is to move `i` or `j` by comparing the end time between two intervals. If one end time is smaller, we know we should update `i := i+1` (since lists are already sorted).

Time Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+m)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n and m is the length of firstList and secondList, respectively.

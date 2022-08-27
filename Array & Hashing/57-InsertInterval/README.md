# Insert Interval

Problem can be found in [here](https://leetcode.com/problems/insert-interval/)!

### [Solution](/Array%20%26%20Hashing/57-InsertInterval/solution.py)

```python
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    merged_intervals = []
    for i, interval in enumerate(intervals):
        if interval[1] < newInterval[0]:
            merged_intervals.append(interval)
        elif interval[0] > newInterval[1]:
            merged_intervals.append(newInterval)
            return merged_intervals + intervals[i:]
        else:
            new_start_time = min(interval[0], newInterval[0])
            new_end_time = max(interval[1], newInterval[1])
            newInterval = [new_start_time, new_end_time]
    merged_intervals.append(newInterval)
    return merged_intervals
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

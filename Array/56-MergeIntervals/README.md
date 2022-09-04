# Merge Intervals

Problem can be found in [here](https://leetcode.com/problems/merge-intervals/)!

### [Solution](/Array/56-MergeIntervals/solution.py)

```python
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    merged_intervals = [intervals[0]]
    for interval in intervals:
        if interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = [merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1])]
        else:
            merged_intervals.append(interval)
    return merged_intervals
```

Explanation: Please refer to this [link](https://github.com/yuchia0221/Grind-75/tree/main/Array/56-MergeIntervals).

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

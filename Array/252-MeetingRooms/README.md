# Meeting Rooms (Not Tested: Leetcode Premium)

Problem can be found in [here](https://leetcode.com/problems/meeting-rooms/)!

### [Solution](/Array/252-MeetingRooms/solution.py)

```python
def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True
```

Explanation: Just look if there exists an overlapped interval.

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

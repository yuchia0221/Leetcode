# Meeting Rooms II (Not Tested: Leetcode Premium)

Problem can be found in [here](https://leetcode.com/problems/meeting-rooms-ii)!

### [Solution](/Array/252-MeetingRooms/solution.py)

```python
def minMeetingRooms(intervals: List[List[int]]) -> int:
    new_intervals = []
    for interval in intervals:
        new_intervals.append([interval[0], 1])
        new_intervals.append([interval[1], -1])

    new_intervals.sort()

    counter = max_overlap = 0
    for _, isMeetingStart in new_intervals:
        counter += isMeetingStart
        max_overlap = max(max_overlap, counter)

    return max_overlap
```

Explanation: We first need to slightly modify the original array. Assume we have an array = [[1, 3], [2, 4], [2, 5]], we need to turn it to [[1, 1], [3, -1], [2, 1], [4, -1], [2, 1], [5, -1]] and sort it ascenedingly. By iterating the mutated array iteratively, we can keep track of the maximum room needed in that span. The second element in each element means whether there is a room required. If the value is 1, meaning that we need a room. If the value is -1, meaning that there will be an available room. In this example, starting from the first inner array, we know that in timestamp 1, there is a need for a room.

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

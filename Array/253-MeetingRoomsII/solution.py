from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
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

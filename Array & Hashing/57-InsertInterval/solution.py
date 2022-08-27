from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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

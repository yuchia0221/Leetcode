from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]
        for interval in intervals:
            if interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1] = [merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1])]
            else:
                merged_intervals.append(interval)
        return merged_intervals

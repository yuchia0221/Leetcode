from sortedcontainers import SortedList
from typing import List


class SummaryRanges:
    def __init__(self):
        self.intervals = SortedList()

    def addNum(self, value: int) -> None:
        n = len(self.intervals)
        i = self.intervals.bisect((value, float("inf")))

        left_interval = self.intervals[i-1] if 0 <= i-1 < n else (float("-inf"), float("-inf"))
        right_interval = self.intervals[i] if 0 <= i < n else (float("inf"), float("inf"))

        if left_interval[0] <= value <= left_interval[1]:
            return

        new_left, new_right = value, value
        if left_interval[1] + 1 == value:
            self.intervals.remove(left_interval)
            new_left = left_interval[0]
        if value == right_interval[0] - 1:
            self.intervals.remove(right_interval)
            new_right = right_interval[1]

        self.intervals.add((new_left, new_right))

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

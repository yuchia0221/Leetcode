from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows, previous = 1, points[0][1]

        for start, end in points:
            if previous < start:
                arrows += 1
                previous = end

        return arrows

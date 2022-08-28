from typing import List


class Solution:
    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
        new_intervals = [j for i in intervals for j in [[i[0], 1], [i[0], -1]]]
        new_intervals.sort()

        start_time = end_time = max_overlap = counter = 0
        for time, room_needed in new_intervals:
            if max_overlap > counter:
                if room_needed == 1:
                    start_time = time
                else:
                    end_time = time
            counter += room_needed
            max_overlap = max(max_overlap, counter)
        
        return max_overlap
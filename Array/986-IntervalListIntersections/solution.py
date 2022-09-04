from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        output_list = []
        while i < len(firstList) and j < len(secondList):
            intersect_start_time = max(firstList[i][0], secondList[j][0])
            intersect_end_time = min(firstList[i][1], secondList[j][1])

            if intersect_start_time <= intersect_end_time:
                output_list.append([intersect_start_time, intersect_end_time])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return output_list
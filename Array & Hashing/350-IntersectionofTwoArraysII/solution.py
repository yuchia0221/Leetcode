from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = defaultdict(int)
        for num in nums1:
            memo[num] += 1

        output_list = []
        for num in nums2:
            if memo[num] > 0:
                output_list.append(num)
                memo[num] -= 1
        
        return output_list

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        number_set = set(nums)

        for num in number_set:
            if num-1 not in number_set:
                current_num = num
                current_streak = 1

                while current_num+1 in number_set:
                    current_num += 1
                    current_streak += 1
                
                longest_sequence = max(longest_sequence, current_streak)
        
        return longest_sequence
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums)-1
        for index in range(len(nums)-1, -1, -1):
            if index + nums[index] >= last_position:
                last_position = index

        return last_position == 0

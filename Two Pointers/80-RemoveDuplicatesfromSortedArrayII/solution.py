from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        slow = fast = 2
        while fast <= len(nums)-1:
            if nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow
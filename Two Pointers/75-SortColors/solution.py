from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, current, blue = 0, 0, len(nums)-1
        while current <= blue:
            if nums[current] == 0:
                nums[red], nums[current] = nums[current], nums[red]
                red += 1
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[current], nums[blue] = nums[blue], nums[current]
                blue -= 1

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output_list = []
        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                left_value, right_value = nums[left], nums[right]
                if left_value + right_value == -num:
                    output_list.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                elif left_value + right_value < -num:
                    left += 1
                else:
                    right -= 1

        return output_list

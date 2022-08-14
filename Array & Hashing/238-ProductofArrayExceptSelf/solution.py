from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = suffix_sum = 1
        output_list = [1] * len(nums)
        for i in range(len(nums)):
            output_list[i] *= prefix_sum
            output_list[-1-i] *= suffix_sum
            prefix_sum *= nums[i]
            suffix_sum *= nums[-1-i]

        return output_list

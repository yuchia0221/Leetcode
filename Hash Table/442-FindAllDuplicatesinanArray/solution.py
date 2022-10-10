from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output_list = []
        for num in nums:
            abs_num = abs(num)
            if nums[abs_num-1] < 0:
                output_list.append(abs_num)
            else:
                nums[abs_num-1] = -nums[abs_num-1]

        return output_list

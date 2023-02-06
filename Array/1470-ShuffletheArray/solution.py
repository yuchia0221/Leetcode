from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output_list = []

        for i in range(n):
            output_list.append(nums[i])
            output_list.append(nums[i+n])

        return output_list

from typing import List


class Solution:
    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        for i in range(len(nums)-1, -1, -1):
            k, nums[i] = divmod(nums[i]+k, 10)

        return [int(i) for i in str(k)] + nums if k else nums

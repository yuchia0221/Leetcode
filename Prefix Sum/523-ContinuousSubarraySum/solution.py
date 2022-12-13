from typing import List


class Solution():
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        prefix_sum = 0
        for i, number in enumerate(nums):
            prefix_sum = (prefix_sum + number) % k
            if prefix_sum not in dic:
                dic[prefix_sum] = i
            else:
                if i - dic[prefix_sum] >= 2:
                    return True

        return False

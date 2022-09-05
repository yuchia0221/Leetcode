from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = defaultdict(int)
        current_sum = number = 0
        for num in nums:
            current_sum += num
            remaining = current_sum - k
            if current_sum == k:
                number += 1
            if remaining in memo:
                number += memo[remaining]

            memo[current_sum] += 1

        return number

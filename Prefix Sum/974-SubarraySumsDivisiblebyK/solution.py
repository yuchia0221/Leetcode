from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = number_of_array = 0
        memo = defaultdict(int)
        memo[0] = 1

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            number_of_array += memo[prefix_sum]
            memo[prefix_sum] += 1

        return number_of_array

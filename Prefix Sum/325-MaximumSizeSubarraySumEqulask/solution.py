from collections import defaultdict
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        memo = defaultdict(int)
        current_sum = max_length = 0
        for i, num in enumerate(nums):
            current_sum += num
            remaining = k - current_sum
            if current_sum == k:
                max_length = i + 1
            elif memo.get(remaining):
                max_length = max(max_length, i-memo[remaining])

            if current_sum not in memo:
                memo[current_sum] = i

        return max_length


def maxSubArrayLen(nums: List[int], k: int) -> int:
    memo = defaultdict(int)
    current_sum = max_length = 0
    for i, num in enumerate(nums):
        current_sum += num
        remaining = current_sum - k
        if current_sum == k:
            max_length = i + 1
        elif remaining in memo:
            max_length = max(max_length, i-memo[remaining])

        if current_sum not in memo:
            memo[current_sum] = i
        print(remaining, memo)

    return max_length


print(maxSubArrayLen([-2, 1, 2, -1, 1], 3))

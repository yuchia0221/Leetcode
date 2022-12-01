from collections import Counter, defaultdict
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        frequency = Counter(nums)
        subsequence = defaultdict(int)
        for num in nums:
            if frequency[num] == 0:
                continue

            frequency[num] -= 1
            if subsequence[num-1] > 0:
                subsequence[num-1] -= 1
                subsequence[num] += 1
            elif frequency[num+1] and frequency[num+2]:
                frequency[num+1] -= 1
                frequency[num+2] -= 1
                subsequence[num+2] += 1
            else:
                return False

        return True

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        for num in nums:
            try:
                memo[num] += 1
            except KeyError:
                memo[num] = 1

        top_k_number = sorted(memo.items(), key=lambda x: x[1], reverse=True)[:k]
        return [i[0] for i in top_k_number]

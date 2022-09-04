from collections import Counter, defaultdict
from itertools import chain
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = defaultdict(list)
        for num, count in Counter(nums).items():
            buckets[count].append(num)

        output_list = []
        for i in range(len(nums), -1, -1):
            output_list.extend(buckets[i])
            if len(output_list) == k:
                break

        return output_list

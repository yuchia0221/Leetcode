from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        counter = Counter(tasks)

        for value in counter.values():
            remainder = value % 3
            if remainder == 0:
                rounds += value // 3
            elif remainder == 1 and value == 1:
                return -1
            else:
                rounds += value // 3 + 1

        return rounds

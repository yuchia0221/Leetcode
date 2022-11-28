from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, songs: List[int]) -> int:
        remainders = defaultdict(int)
        number_of_pairs, divisor = 0, 60

        for time in songs:
            if time % divisor == 0:
                number_of_pairs += remainders[0]
            else:
                number_of_pairs += remainders[divisor-time % divisor]
            remainders[time % divisor] += 1

        return number_of_pairs

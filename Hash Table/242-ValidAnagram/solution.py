from collections import defaultdict
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo = defaultdict(int)
        for char in s:
            memo[char] += 1

        for char in t:
            if memo[char] == 0:
                return False
            memo[char] -= 1

        return all(count == 0 for count in memo.values())

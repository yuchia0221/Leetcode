from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        for string in strs:
            sorted_string = "".join(sorted(string))
            memo[sorted_string].append(string)

        return memo.values()

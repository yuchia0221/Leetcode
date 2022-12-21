from functools import cache
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def generate_paritions(string: str) -> List[str]:
            if not string:
                return [[]]

            paritions = []
            for end in range(1, len(string)+1):
                partial_string = string[:end]
                if partial_string == partial_string[::-1]:
                    for parition in generate_paritions(string[end:]):
                        paritions.append([partial_string] + parition)

            return paritions

        return generate_paritions(s)

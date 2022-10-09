from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @cache
        def work_break_healper(string: str) -> List[List[str]]:
            if not string:
                return [[]]

            combinations = []
            for length in range(1, len(string)+1):
                word = string[:length]
                if word in word_set:
                    for sub_word in work_break_healper(string[length:]):
                        combinations.append([word] + sub_word)

            return combinations

        word_set = set(wordDict)
        result = work_break_healper(s)
        return [" ".join(i) for i in result]

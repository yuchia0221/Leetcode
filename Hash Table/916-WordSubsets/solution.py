from collections import Counter, defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = defaultdict(int)
        for word in words2:
            char_set = Counter(word)
            for key, value in char_set.items():
                counter[key] = max(counter[key], value)

        matched_words = []
        for word in words1:
            char_set = Counter(word)
            for key, value in counter.items():
                if char_set[key] < value:
                    break
            else:
                matched_words.append(word)

        return matched_words

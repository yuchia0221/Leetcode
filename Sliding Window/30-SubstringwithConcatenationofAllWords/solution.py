from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        matched_positions = []
        word_length = len(words[0])
        total_length = word_length * len(words)

        for start in range(word_length):
            i = start
            counter = Counter(words)

            for j in range(i, len(s)+1-word_length, word_length):
                word = s[j:j+word_length]
                counter[word] -= 1

                while counter[word] < 0:
                    counter[s[i:i+word_length]] += 1
                    i += word_length
                if i + total_length == j + word_length:
                    matched_positions.append(i)

        return matched_positions

from collections import defaultdict
from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similar_words = defaultdict(set)
        for word1, word2 in similarPairs:
            similar_words[word1].add(word2)
            similar_words[word2].add(word1)

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in similar_words[sentence1[i]]:
                continue
            return False

        return True

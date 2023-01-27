from typing import List, Set


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(word: str, wordset: Set[str]) -> bool:
            if word == "":
                return True
            for i in range(len(word)):
                if word[:i+1] in wordset:
                    if dfs(word[i+1:], wordset):
                        return True
            return False

        result = []
        wordset = set(words)
        for word in words:
            wordset.remove(word)
            if dfs(word, wordset):
                result.append(word)
            wordset.add(word)

        return result

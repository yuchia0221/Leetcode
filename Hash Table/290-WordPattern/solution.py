class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
            return False

        word_to_pattern = dict()
        for char, word in zip(pattern, words):
            if word not in word_to_pattern:
                word_to_pattern[word] = char
            elif word_to_pattern[word] != char:
                return False

        return True

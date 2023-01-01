# Word Pattern

Problem can be found in [here](https://leetcode.com/problems/word-pattern/)!

### [Solution](/Hash%20Table/290-WordPattern/solution.py): Hash Table

```python
def wordPattern(pattern: str, s: str) -> bool:
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

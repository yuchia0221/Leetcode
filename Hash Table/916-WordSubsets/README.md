# Word Subsets

Problem can be found in [here](https://leetcode.com/problems/word-subsets/)!

### [Solution](/Hash%20Table/916-WordSubsets/solution.py): Hash Table

```python
def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
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
```

Time Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+m)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n and m are the total number of characters in words1 and words2, respectively.

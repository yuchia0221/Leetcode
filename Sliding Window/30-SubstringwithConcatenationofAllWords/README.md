# Substring with Concatenation of All Words

Problem can be found in [here](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)!

### [Solution](/Sliding%20Window/30-SubstringwithConcatenationofAllWords/solution.py)

```python
def findSubstring(s: str, words: List[str]) -> List[int]:
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
```

Time Complexity: ![O(n^2*(a+m))](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2\cdot(a+m))>), Space Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), where the size of each word in the array words is n, the length of array words is m, and the length of string s is k.

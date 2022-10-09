# Integer Break

Problem can be found in [here](https://leetcode.com/problems/word-break-ii/)!

### [Solution](/Dynamic%20Programming/140-WordBreakII/solution.py): Dynamic Programming

```python
def wordBreak(s: str, wordDict: List[str]) -> List[str]:
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
```

Time Complexity: ![O(n^k)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^k)>), Space Complexity: ![O(n^k)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where k is the length of the answer array.
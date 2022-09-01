# Longest Substring Without Repeating Characters

Problem can be found in [here](https://leetcode.com/problems/longest-substring-without-repeating-characters/)!

### [Solution](/String/3-LongestSubstringWithoutRepeatingCharacters/solution.py)

```python
def lengthOfLongestSubstring(s: str) -> int:
    memo = set()
    window_start = window_end = max_length = 0

    while window_start < len(s) and window_end < len(s):
        token = s[window_end]
        if token in memo:
            memo.remove(s[window_start])
            window_start += 1
        else:
            window_end += 1
            max_length = max(max_length, window_end-window_start)
            memo.add(token)

    return max_length
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O()>)

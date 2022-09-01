# Minimum Window Substring

Problem can be found in [here](https://leetcode.com/problems/minimum-window-substring/)!

### [Solution](/Array%20%26%20Hashing/76-MinimumWindowSubstring/solution.py): Hash Table + Sliding Window

```python
def minWindow(s: str, t: str) -> str:
    missing_counter = len(t)
    window_start = window_end = current = 0
    memo = collections.Counter(t)

    for index, token in enumerate(s, 1):
        # Expand to find a valid window
        if memo[token] > 0:
            missing_counter -= 1
        memo[token] -= 1

        # Find a valid window
        if missing_counter == 0:
            # Contract to find a smaller and valid window
            while memo[s[current]] < 0:
                memo[s[current]] += 1
                current += 1

            if window_end == 0 or index-current < window_end-window_start:
                window_start, window_end = current, index

            # Move forward to find a new window
            memo[s[current]] += 1
            missing_counter += 1
            current += 1

    return s[window_start:window_end]
```

Explanation: We can use a hash map to count if we satisfies the substring. Whenever we find we satisfies the requirement of substring t, we can perform a sliding window to find whether there exists a smaller substring that also meets the requirement of substring t.

Time Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n and m is the length of s and t, respectively.

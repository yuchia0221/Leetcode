# Longest Palindromic Subsequence

Problem can be found in [here](https://leetcode.com/problems/longest-palindromic-subsequence/)!

### [Solution](/Dynamic%20Programming/516-LongestPalindromicSubsequence/solution.py): Dynamic Programming

```python
def longestPalindromeSubseq(s: str) -> int:
    @cache
    def dp(l, r):
        if l > r:
            return 0
        if l == r:
            return 1
        if s[l] == s[r]:
            return dp(l+1, r-1) + 2

        return max(dp(l, r-1), dp(l+1, r))

    n = len(s)
    return dp(0, n-1)
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>)

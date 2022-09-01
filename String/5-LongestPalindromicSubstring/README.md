# Longest Palindromic Substring

Problem can be found in [here](https://leetcode.com/problems/longest-palindromic-substring/)!

### [Solution](/String/5-LongestPalindromicSubstring/solution.py)

```python
def longestPalindrome(s: str) -> str:
    longest_palindrome = s[0]
    memo = [[False] * len(s) for i in range(len(s))]

    for i in range(len(s)):
        memo[i][i] = True

    # P[i,j] = P(i+1,j-1) + S[i] == S[j]
    for i in range(len(s)):
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                if i == j+1 or memo[i-1][j+1]:
                    memo[i][j] = True
                    if i-j+1 > len(longest_palindrome):
                        longest_palindrome = s[j:i+1]

    return longest_palindromedef longestPalindrome(s: str) -> str:
    longest_palindrome = s[0]
    memo = [[False] * len(s) for i in range(len(s))]

    for i in range(len(s)):
        memo[i][i] = True

    # P[i,j] = P(i+1,j-1) + S[i] == S[j]
    for i in range(len(s)):
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                if i == j+1 or memo[i-1][j+1]:
                    memo[i][j] = True
                    if i-j+1 > len(longest_palindrome):
                        longest_palindrome = s[j:i+1]

    return longest_palindrome
```

Explanation: Consider the case "ababa". If we already knew that "bab" is a palindrome, it is obvious that "ababa" must be a palindrome since the two left and right end letters are the same.

The recursion function is $P(i,j)=P(i+i,j-1)+(s[i]==s[j)]$, where $P(i, i) = true$.

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>)

# Valid Palindrome II

Problem can be found in [here](https://leetcode.com/problems/valid-palindrome-ii/)!

### [Solution](/String/680-ValidPalindromeII/solution.py): Two Pointers

```python
def validPalindrome(s: str) -> bool:
    def isPalindrome(string: str):
        return string == string[::-1]

    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            delete_left, delete_right = s[left+1:right+1], s[left:right]
            return isPalindrome(delete_left) or isPalindrome(delete_right)

        left += 1
        right -= 1

    return True
```

Explanation: We can apply two pointers to solve this problem. One pointer starts form the left end of a string and the other starts from the right end of that. In each iteration, if we find s[i] ≠ s[j], then we can simply look for is s[i+1:j+1] or s[i:j] is a palindrome. If both of them are not, return False; otherwise return True. This strategy is correct because we can only remove 1 character.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

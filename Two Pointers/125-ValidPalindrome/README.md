# Valid Palindrome

Problem can be found in [here](https://leetcode.com/problems/valid-palindrome/)!

### [Solution](/Two%20Pointers/125-ValidPalindrome/solution.py): Two Pointers

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

Explanation: Please refer to [link](https://github.com/yuchia0221/Grind-75/tree/main/String/125-ValidPalindrome) for explanation.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

# Break a Palindrome

Problem can be found in [here](https://leetcode.com/problems/break-a-palindrome/)!

### [Solution](/String/13-RomantoInteger/solution.py)

```python
def breakPalindrome(palindrome: str) -> str:
    if len(palindrome) == 1:
        return ""

    string = list(palindrome)
    for index in range(len(string) // 2):
        if string[index] != "a":
            string[index] = "a"
            break
    else:
        string[-1] = "b"

    return "".join(string)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

# Minimum Remove to Make Valid Parentheses

Problem can be found in [here](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)!

### [Solution](/Stack/1249-MinimumRemovetoMakeValidParentheses/solution.py): Stack

```python
def minRemoveToMakeValid(s: str) -> str:
    stack = []
    string = list(s)
    for index, char in enumerate(s):
        if char == "(":
            stack.append(index)
        elif char == ")":
            if not stack or s[stack[-1]] != "(":
                string[index] = ""
            else:
                stack.pop()

        else:
            continue

    while stack:
        string[stack.pop()] = ""

    return "".join(string)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

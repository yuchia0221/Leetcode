# Detect Capital

Problem can be found in [here](https://leetcode.com/problems/detect-capital/)!

### [Solution](/String/520-DetectCapital/solution.py)

```python
def detectCapitalUse(word: str) -> bool:
    if len(word) == 1:
        return True

    if word[0].isupper() and word[1].isupper():
        for i in range(2, len(word)):
            if not word[i].isupper():
                return False
    else:
        for i in range(1, len(word)):
            if word[i].isupper():
                return False

    return True
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

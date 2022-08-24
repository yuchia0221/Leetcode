# Multiply Strings

Problem can be found in [here](https://leetcode.com/problems/multiply-strings/)!

### [Solution](/Two%20Pointers/43-MultiplyStrings/solution.py): Two Pointers

```python
def multiply(num1: str, num2: str) -> str:
    result = 0
    for i in range(len(num1)-1, -1, -1):
        base = pow(10, len(num1)-i-1)
        for j in range(len(num2)-1, -1, -1):
            result += int(num1[i]) * int(num2[j]) * base
            base *= 10

    return str(result)
```


Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n and m is the length of string num1 and num2, respectively.

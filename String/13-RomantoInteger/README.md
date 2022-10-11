# Roman to Integer

Problem can be found in [here](https://leetcode.com/problems/roman-to-integer/)!

### [Solution](/String/13-RomantoInteger/solution.py)

```python
def romanToInt(s: str) -> int:
    total = index = 0
    char_to_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    while index < len(s):
        if index+1 < len(s) and s[index:index+2] in char_to_number:
            total += char_to_number[s[index:index+2]]
            index += 2
        else:
            total += char_to_number[s[index]]
            index += 1

    return total
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

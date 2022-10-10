# Zigzag Conversion

Problem can be found in [here](https://leetcode.com/problems/zigzag-conversion/)!

### [Solution](/String/6-ZigzagConversion/solution.py)

```python
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    zipzag_string = ""
    cycle = 2*numRows - 2
    for i in range(numRows):
        for j in range(0, len(s), cycle):
            if i + j >= len(s):
                break
            zipzag_string += s[i + j]
            if (i != 0 and i != numRows-1 and j+cycle-i < len(s)):
                zipzag_string += s[j+cycle-i]

    return zipzag_string
```

Explanation: If we try to append characters in sequence without using additional memory,
row(0, k) = character at index (k-1) (2n-2)
row(i, k) = characters at indexes (k-1)(2n-2) + i and (k-1)(2n-2)+(2n-2-i)
row(n-1, k) = character at index (k-1)(2n-2)+(n-1)
where k means elements in that row for cycle k.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

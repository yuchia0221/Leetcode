# Decode Ways

Problem can be found in [here](https://leetcode.com/problems/decode-ways/)!

### [Solution](/Dynamic%20Programming/91-DecodeWays/solution.py): Dynamic Programming

```python
def numDecodings(s: str) -> int:
    @cache
    def decoder(index: int) -> int:
        if index == len(s):
            return 1

        valid_decoding_ways = 0
        if 1 <= int(s[index]) <= 26:
            valid_decoding_ways += decoder(index+1)
        if index < len(s)-1 and s[index] != "0" and 1 <= int(s[index:index+2]) <= 26:
            valid_decoding_ways += decoder(index+2)

        return valid_decoding_ways

    return decoder(0)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

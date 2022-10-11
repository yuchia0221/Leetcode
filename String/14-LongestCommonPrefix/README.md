# Longest Common Prefix

Problem can be found in [here](https://leetcode.com/problems/longest-common-prefix/)!

### [Solution](/String/14-LongestCommonPrefix/solution.py)

```python
def longestCommonPrefix(strs: List[str]) -> str:
    common_prefix = ""
    for chars in zip(*strs):
        if len(set(chars)) == 1:
            common_prefix += chars[0]

    return common_prefix
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

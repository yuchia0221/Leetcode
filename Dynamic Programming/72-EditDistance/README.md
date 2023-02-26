# Edit Distance

Problem can be found in [here](https://leetcode.com/problems/edit-distance/)!

### [Solution](/Dynamic%20Programming/72-EditDistance/solution.py): Dynamic Programming

```python
def minDistance(s1: str, s2: str) -> int:
    @cache
    def dp(i: int, j: int) -> int:
        if i == 0:
            return j
        if j == 0:
            return i

        if s1[i-1] == s2[j-1]:
            return dp(i-1, j-1)

        return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1

    return dp(len(s1), len(s2))
```

Time Complexity: ![O(mn)](<https://latex.codecogs.com/svg.image?\inline&space;O(mn)>), Space Complexity: ![O(mn)](<https://latex.codecogs.com/svg.image?\inline&space;O(mn)>), where m and n are the length of string s1 and s2, respectively.

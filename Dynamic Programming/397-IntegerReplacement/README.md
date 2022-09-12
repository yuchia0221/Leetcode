# Integer Replacement

Problem can be found in [here](https://leetcode.com/problems/integer-break/)!

### [Solution](/Dynamic%20Programming/397-IntegerReplacement/solution.py): Dynamic Programming

```python
@lru_cache
def integerReplacement(n: int) -> int:
    if n == 1:
        return 0
    if is_number_even(n):
        return integerReplacement(n // 2) + 1
    else:
        return min(integerReplacement(n-1), integerReplacement(n+1)) + 1

def is_number_even(num):
    return num % 2 == 0
```

Explanation: The DP recursion function is easy. If i is an even number, `dp[i] = dp[i / 2] + 1`. Otherwise, `dp[i] = min(dp[i+1], dp[i-1]) + 1`.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

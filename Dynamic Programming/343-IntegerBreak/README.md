# Integer Break

Problem can be found in [here](https://leetcode.com/problems/integer-break/)!

### [Solution](/Dynamic%20Programming/343-IntegerBreak/solution.py): Dynamic Programming

```python
def integerBreak(n: int) -> int:
    memo = [i for i in range(n+1)]
    memo[n] = 0

    for i in range(2, n+1):
        for j in range(1, i):
            memo[i] = max(memo[i], memo[j] * memo[i-j])

    return memo[n]
```

Explanation: Observe that if we want to get the maximum product (without the need of breaking the integer into several smaller integers) for n ≤ 5, we will get the value itself. However, if we need to know integerBreak(n) for n ≤ 5 (we need splitting integer now), the value will be smaller than value itself because we have to split integers into at least two pieces. That is the reason we need to initialize the value of memo[n] = 0 because it needs to break into at least two pieces. We can use write down the equation to solve this problem: dp[i] = max(dp[i], dp[j]\*d[i-j]) for 1 ≤ j < i.

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

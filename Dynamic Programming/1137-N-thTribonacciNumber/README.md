# N-th Tribonacci Number

Problem can be found in [here](https://leetcode.com/problems/n-th-tribonacci-number/)!

### [Solution](/Dynamic%20Programming/1137-N-thTribonacciNumber/solution.py): Dynamic Programming

```python
@cache
def tribonacci(self, n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

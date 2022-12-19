# Sum of Subarray Minimums

Problem can be found in [here](https://leetcode.com/problems/sum-of-subarray-minimums/)!

### [Solution](/Dynamic%20Programming/907-SumofSubarrayMinimums/solution.py): Dynamic Programming

```python
def sumSubarrayMins(arr: List[int]) -> int:
    stack = []
    dp = [0] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if stack:
            previous_smaller = stack[-1]
            dp[i] = dp[previous_smaller] + (i-previous_smaller) * arr[i]
        else:
            dp[i] = (i+1) * arr[i]

        stack.append(i)

    return sum(dp) % (pow(10, 9) + 7)
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

# Binary Trees With Factors

Problem can be found in [here](https://leetcode.com/problems/binary-trees-with-factors/)!

### [Solution](/Dynamic%20Programming/823-BinaryTreesWithFactors/solution.py): Dynamic Programming

```python
def numFactoredBinaryTrees(arr: List[int]) -> int:
    arr.sort()
    dp = [1] * len(arr)
    index = {number: i for i, number in enumerate(arr)}

    for i, number in enumerate(arr):
        for j in range(i):
            if number % arr[j] == 0:
                right = number / arr[j]
                if right in index:
                    dp[i] += dp[j] * dp[index[right]]

    return sum(dp) % (pow(10, 9) + 7)
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

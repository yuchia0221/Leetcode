# Factor Combinations

Problem can be found in [here](https://leetcode.com/problems/factor-combinations/)!

### [Solution](/Backtracking/254-FactorCombinations/solution.py): Backtracking

```python
def getFactors(n: int) -> List[List[int]]:
    def helper(factors: List[int], least_factor: int, target: int):
        if len(factors) > 0:
            result.append(factors + [target])
        for candidate_factor in range(least_factor, int(sqrt(target))+1):
            if target % candidate_factor == 0:
                helper(factors+[candidate_factor], candidate_factor, target // candidate_factor)

    result = []
    if n == 1:
        return result
    helper([], 2, n)
    return result
```

Explanation: We can use the backtracking technique to solve this problem. We will append valid factor into the factors list ascendingly to avoid duplicated factor combinations. If n = 12, we will only append [2, 2, 3] but not [2, 3, 2] with the help of a variable called least_factor.

Time Complexity: ![O(logn*logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn*logn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

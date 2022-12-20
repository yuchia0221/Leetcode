# Number of Dice Rolls With Target Sum

Problem can be found in [here](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)!

### [Solution](/Dynamic%20Programming/1155-NumberofDiceRollsWithTargetSum/Solution.py): Dynamic Programming

```python
def numRollsToTarget(d: int, f: int, target: int) -> int:
    @cache
    def dp(d: int, target: int) -> int:
        if d == 0:
            return 0 if target > 0 else 1

        value = 0
        for k in range(max(0, target-f), target):
            value += dp(d-1, k)

        return value

    return dp(d, target) % (pow(10, 9) + 7)
```

Time Complexity: ![O(dft)](<https://latex.codecogs.com/svg.image?\inline&space;O(dft)>), Space Complexity: ![O(dt)](<https://latex.codecogs.com/svg.image?\inline&space;O(dt)>), where d is the number of dices, f is the number of faces each dice have, and t is the target value.

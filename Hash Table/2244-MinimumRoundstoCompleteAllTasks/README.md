# Minimum Rounds to Complete All Tasks

Problem can be found in [here](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/)!

### [Solution](/Hash%20Table/2244-MinimumRoundstoCompleteAllTasks/solution.py): Hash Table

```python
def minimumRounds(tasks: List[int]) -> int:
    rounds = 0
    counter = Counter(tasks)

    for value in counter.values():
        remainder = value % 3
        if remainder == 0:
            rounds += value // 3
        elif remainder == 1 and value == 1:
            return -1
        else:
            rounds += value // 3 + 1

    return rounds
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

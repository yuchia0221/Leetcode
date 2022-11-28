# Reorder Data in Log Files

Problem can be found in [here](https://leetcode.com/problems/reorder-data-in-log-files/)!

### [Solution](/Array/937-ReorderDatainLogFiles/solution.py): Sorting

```python
def reorderLogFiles(logs: List[str]) -> List[str]:
    letter_logs, digit_logs = [], []

    for log in logs:
        new_log = log.split(" ", 1)
        if new_log[1][0].isnumeric():
            digit_logs.append(log)
        else:
            letter_logs.append((new_log[0], new_log[1]))

    letter_logs.sort(key=lambda x: (x[1], x[0]))
    sorted_letter_logs = [f"{key} {value}" for key, value in letter_logs]

    return sorted_letter_logs + digit_logs
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>)

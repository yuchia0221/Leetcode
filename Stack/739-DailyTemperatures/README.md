# Daily Temperatures

Problem can be found in [here](https://leetcode.com/problems/daily-temperatures/)!

### [Solution](/Stack/739-DailyTemperatures/solution.py): Monotonic Stack

```python
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    days_to_wait = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            index = stack.pop()
            days_to_wait[index] = i-index

        stack.append(i)

    return days_to_wait
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

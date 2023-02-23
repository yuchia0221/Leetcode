# IPO

Problem can be found in [here](https://leetcode.com/problems/ipo/)!

### [Solution](/Heap/502-IPO/solution.py): Heap

```python
def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    n = len(profits)
    projects = sorted(zip(capital, profits))
    max_heap = []
    pointer = 0
    for _ in range(k):
        while pointer < n and projects[pointer][0] <= w:
            heappush(max_heap, -projects[pointer][1])
            pointer += 1
        if not max_heap:
            break

        w += -heappop(max_heap)

    return w
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of array profits.

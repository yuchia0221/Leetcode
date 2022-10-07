# The Skyline Problem

Problem can be found in [here](https://leetcode.com/problems/the-skyline-problem/)!

### [Solution](/Heap/218-TheSkylineProblem/solution.py): Heap

```python
def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    live, past = [], []
    edges, result = [], []
    for left, right, height in buildings:
        edges.append([left, height])
        edges.append([right, -height])
    edges.sort()
    index = 0
    while index < len(edges):
        current_x = edges[index][0]
        while index < len(edges) and edges[index][0] == current_x:
            height = edges[index][1]
            if height > 0:
                heappush(live, -height)
            else:
                heappush(past, height)

            index += 1

        while past and past[0] == live[0]:
            heappop(live)
            heappop(past)

        max_height = -live[0] if live else 0
        if not result or result[-1][1] != max_height:
            result.append([current_x, max_height])

    return result
```


Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of the buildings array.

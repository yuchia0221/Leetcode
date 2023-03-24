# Reorder Routes to Make All Paths Lead to the City Zero

Problem can be found in [here](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)!

### [Solution](/Depth-first%20Search/1466-ReorderRoutestoMakeAllPathsLeadtotheCityZero/solution.py)

```python
def minReorder(n: int, connections: List[List[int]]) -> int:
    def dfs(current: int, parent: int) -> int:
        nonlocal count
        for neighbor, is_origin_path in graph[current]:
            if neighbor != parent:
                count += is_origin_path
                dfs(neighbor, current)

    count = 0
    graph = defaultdict(list)
    for src, dest in connections:
        graph[src].append((dest, 1))
        graph[dest].append((src, 0))

    dfs(0, -1)
    return count
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>).

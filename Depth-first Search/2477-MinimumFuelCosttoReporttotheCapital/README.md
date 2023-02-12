# Minimum Fuel Cost to Report to the Capital

Problem can be found in [here](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/)!

### [Solution](/Depth-first%20Search/2477-MinimumFuelCosttoReporttotheCapital/solution.py)

```python
def minimumFuelCost(roads: List[List[int]], seats: int) -> int:
    def dfs(node: int) -> int:
        nonlocal answer
        subtree_size = 1
        for neighbor in graph[node]:
            if neighbor not in vistied:
                vistied.add(node)
                subtree_size += dfs(neighbor)
        if node != 0:
            answer += math.ceil(subtree_size / seats)
        return subtree_size

    graph = defaultdict(list)
    for src, dest in roads:
        graph[src].append(dest)
        graph[dest].append(src)

    answer = 0
    vistied = set()
    dfs(0)
    return answer
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

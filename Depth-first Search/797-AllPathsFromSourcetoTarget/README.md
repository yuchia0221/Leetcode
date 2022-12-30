# All Paths From Source to Target

Problem can be found in [here](https://leetcode.com/problems/all-paths-from-source-to-target/)!

### [Solution](/Depth-first%20Search/210-CourseScheduleII/solution.py): Depth-first Search

```python
def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    def dfs(node: int, path: List[int]) -> None:
        if node == target:
            paths.append(path)

        for neighbor in graph[node]:
            dfs(neighbor, path+[neighbor])

    paths = []
    target = len(graph)-1
    dfs(0, [0])
    return paths
```

Time Complexity: ![O(V+E)](<https://latex.codecogs.com/svg.image?\inline&space;O(V+E)>), Space Complexity: ![O(V+E)](<https://latex.codecogs.com/svg.image?\inline&space;O(V+E)>), where V is the number of courses and E is the length of prerequisites.

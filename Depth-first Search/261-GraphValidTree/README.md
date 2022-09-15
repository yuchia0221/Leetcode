# Graph Valid Tree

Problem can be found in [here](https://leetcode.com/problems/graph-valid-tree/)!

### [Solution](/Depth-first%20Search/210-CourseScheduleII/solution.py): Depth-first Search

```python
def validTree(n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    stack = [0]
    visited_nodes = set([0])
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor in visited_nodes:
                continue
            visited_nodes.add(neighbor)
            stack.append(neighbor)

    return len(visited_nodes) == n
```

Explanation: Graph`G`, **is a tree iff** the following two conditions are met:

1. `G` is fully connected. In other words, for every pair of nodes in `G`, there is a path between them.
2. `G` contains no cycles. In other words, there is exactly *one* path between each pair of nodes in `G`.

→ Summarize two conditions, we can get there must be |V|-1 edges in the graph and every nodes should be connected

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the number of vertexes

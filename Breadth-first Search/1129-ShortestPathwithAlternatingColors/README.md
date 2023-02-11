# Shortest Path with Alternating Colors

Problem can be found in [here](https://leetcode.com/problems/shortest-path-with-alternating-colors/)!

### [Solution](/Breadth-first%20Search/1129-ShortestPathwithAlternatingColors/solution.py): Breadth-first Search

```python
def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    graph = defaultdict(lambda: defaultdict(list))
    for src, dest in redEdges:
        graph["red"][src].append(dest)
    for src, dest in blueEdges:
        graph["blue"][src].append(dest)

    step = 0
    distances = [-1] * n
    visited = set([(0, "r"), (0, "b")])
    queue = deque([(0, "r"), (0, "b")])
    while queue:
        for _ in range(len(queue)):
            node, color = queue.popleft()
            if distances[node] == -1:
                distances[node] = step
            else:
                distances[node] = min(distances[node], step)

            if color == "r":
                for neighbor in graph["blue"][node]:
                    edge = (neighbor, "b")
                    if edge not in visited:
                        queue.append(edge)
                        visited.add(edge)
            else:
                for neighbor in graph["red"][node]:
                    edge = (neighbor, "r")
                    if edge not in visited:
                        queue.append(edge)
                        visited.add(edge)

        step += 1

    return distances
```

Time Complexity: ![O(v+n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(v+n+m)>), Space Complexity: ![O(v+n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(v+n+m)>), where v is the number of nodes and n and m are the length of array redEdges and blueEdges, respectively.

# Find Closest Node to Given Two Nodes

Problem can be found in [here](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/)!

### [Solution](/Breadth-first%20Search/2359-FindClosestNodetoGivenTwoNodes/solution.py): Breadth-first Search

```python
def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    def bfs(root: int, distance: List[int]) -> None:
        visited = set([root])
        queue = deque([[root, 0]])

        while queue:
            node, step = queue.popleft()
            next_node = edges[node]
            distance[node] = min(distance[node], step)
            if next_node not in visited and next_node != -1:
                visited.add(next_node)
                queue.append((next_node, step+1))

    n = len(edges)
    node1_distance, node2_distance = [float("inf")]*n, [float("inf")]*n
    bfs(node1, node1_distance)
    bfs(node2, node2_distance)

    closet_node = -1
    smallest_distance = float("inf")
    for index, (distance1, distance2) in enumerate(zip(node1_distance, node2_distance)):
        if max(distance1, distance2) < smallest_distance:
            closet_node = index
            smallest_distance = max(distance1, distance2)

    return closet_node
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the number of nodes in the grpah.

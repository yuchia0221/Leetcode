# Alien Dictionary

Problem can be found in [here](https://leetcode.com/problems/alien-dictionary/)!

### [Solution](/Depth-first%20Search/269-AlienDictionary/solution.py): Topological Sort

```python
def alienOrder(words: List[str]) -> str:
    graph = defaultdict(set)
    in_degree = Counter({c: 0 for word in words for c in word})

    for i in range(len(words)-1):
        for char1, char2 in zip(words[i], words[i+1]):
            if char1 != char2:
                if char2 not in graph[char1]:
                    graph[char1].add(char2)
                    in_degree[char2] += 1
                break
        else:
            if len(words[i+1]) < len(words[i]):
                return ""

    alien_dictionary = ""
    zero_incoming_edges = deque([char for char in in_degree if in_degree[char] == 0])
    while zero_incoming_edges:
        vertex = zero_incoming_edges.popleft()
        alien_dictionary += vertex
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_incoming_edges.append(neighbor)

    return alien_dictionary if len(alien_dictionary) >= len(in_degree) else ""
```

Explanation: After we construct the graph and compute the number of incoming edges for every comparable characters in words, we can perform a topological sort to check if a cycle exists. If so, we cannot deduce the correct order of the alien dictionary.

Time Complexity: ![O(V+E)](<https://latex.codecogs.com/svg.image?\inline&space;O(V+E)>), Space Complexity: ![O(V)](<https://latex.codecogs.com/svg.image?\inline&space;O(V)>), where V is the length of words and E is the number of edges in the graph.

# Longest Path With Different Adjacent Characters

Problem can be found in [here](https://leetcode.com/problems/longest-path-with-different-adjacent-characters/)!

### [Solution](/Depth-first%20Search/2246-LongestPathWithDifferentAdjacentCharacters/solution.py)

```python
def longestPath(parent: List[int], s: str) -> int:
    children = defaultdict(list)
    for i, j in enumerate(parent):
        if j >= 0:
            children[j].append(i)

    longest_path = 0

    def dfs(node: int) -> int:
        nonlocal longest_path
        max1 = max2 = 0
        for neighbor in children[node]:
            neighbor_path = dfs(neighbor)
            if s[node] != s[neighbor]:
                if neighbor_path > max1:
                    max1, max2 = neighbor_path, max1
                elif neighbor_path > max2:
                    max2 = neighbor_path

        longest_path = max(longest_path, max1+max2+1)
        return max1+1

    dfs(0)
    return longest_path
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), wheren is the length of array parent.

# Evaluate Division

Problem can be found in [here](https://leetcode.com/problems/evaluate-division/)!

### [Solution](/Union%20Find/399-EvaluateDivision/solution.py): Disjoint Set

```python
class DisjointSet:
    def __init__(self) -> None:
        self.parent = {}

    def find(self, x: str) -> Tuple[str, int]:
        if x not in self.parent:
            self.parent[x] = [x, 1]
        parent_x, weight = self.parent[x]
        if parent_x != x:
            real_parent, new_weight = self.find(parent_x)
            self.parent[x] = [real_parent, weight * new_weight]

        return self.parent[x]

    def union(self, dividend: str, divisor: str, value: int):
        root_dividend, weight_dividend = self.find(dividend)
        root_divisor, weight_divisor = self.find(divisor)

        if root_dividend != root_divisor:
            self.parent[root_dividend] = [root_divisor, weight_divisor * value / weight_dividend]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        disjoint_set = DisjointSet()
        for (dividend, divisor), value in zip(equations, values):
            disjoint_set.union(dividend, divisor, value)

        for dividend, divisor in queries:
            if dividend not in disjoint_set.parent or divisor not in disjoint_set.parent:
                result.append(-1)
            else:
                root_dividend, weight_dividend = disjoint_set.find(dividend)
                root_divisor, weight_divisor = disjoint_set.find(divisor)
                if root_dividend != root_divisor:
                    result.append(-1)
                else:
                    result.append(weight_dividend/weight_divisor)

        return result
```

Time Complexity: ![O((N+M)a(N))](<https://latex.codecogs.com/svg.image?\inline&space;O((N+M))\cdot&space;\alpha&space;(N))>), Space Complexity: ![O(N)](<https://latex.codecogs.com/svg.image?\inline&space;O(N)>), where $N$ is the number of input equations and $M$ is the number of queries.

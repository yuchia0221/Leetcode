# Find the Celebrity

Problem can be found in [here](https://leetcode.com/problems/find-the-celebrity/)!

### [Solution](/Breadth-first%20Search/277-FindtheCelebrity/solution.py)

```python
class Solution:
    @cache
    def cached_knows(self, a: int, b: int) -> bool:
        return knows(a, b)

    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if self.cached_knows(candidate, i):
                candidate = i

        if self.is_celebrity(candidate, n):
            return candidate
        return -1

    def is_celebrity(self, candidate: int, n: int) -> bool:
        for i in range(n):
            if i == candidate:
                continue
            if self.cached_knows(candidate, i) or not self.cached_knows(i, candidate):
                return False
        return True
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

# Random Pick with Weight

Problem can be found in [here](https://leetcode.com/problems/random-pick-with-weight/)!

### [Solution](/Prefix%20Sum/528-RandomPickwithWeight/solution.py): Prefix Sum

```python
class Solution:
    def __init__(self, w: List[int]):
        self.weights = w
        for i in range(1, len(w)):
            self.weights[i] += self.weights[i-1]

    def pickIndex(self) -> int:
        random_number = randint(1, self.weights[-1])

        # return bisect.bisect_left(self.weights)
        return self.binary_search(random_number)

    @lru_cache
    def binary_search(self, number: int) -> int:
        left, right = 0, len(self.weights)
        while left < right:
            mid = (left+right) // 2
            if number <= self.weights[mid]:
                right = mid
            else:
                left = mid + 1

        return left
```

Explanation: First, compute the cumulative density function by using prefix sum techniques. Generate a random integer from 1 to the sum of the w. Perform a binary search to locate which value should we return.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

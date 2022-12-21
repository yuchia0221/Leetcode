# Palindrome Partitioning

Problem can be found in [here](https://leetcode.com/problems/palindrome-partitioning/)!

### [Solution](/Backtracking/131-PalindromePartitioning/solution.py): Backtracking + Memorization

```python
def partition(s: str) -> List[List[str]]:
    @cache
    def generate_paritions(string: str) -> List[str]:
        if not string:
            return [[]]

        paritions = []
        for end in range(1, len(string)+1):
            partial_string = string[:end]
            if partial_string == partial_string[::-1]:
                for parition in generate_paritions(string[end:]):
                    paritions.append([partial_string] + parition)

        return paritions

    return generate_paritions(s)
```

Time Complexity: ![O(n*2^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n*2^n)>), Space Complexity: ![O(n*2^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n*2^n)>)

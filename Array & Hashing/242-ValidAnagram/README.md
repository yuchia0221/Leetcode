# Valid Anagram

Problem can be found in [here](https://leetcode.com/problems/valid-anagram/)!

### [Solution](/Array%20%26%20Hashing/242-ValidAnagram/solution.py): Hash Table

```python
def isAnagram(s: str, t: str) -> bool:
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1

    for char in t:
        if memo[char] == 0:
            return False
        memo[char] -= 1

    return all(count == 0 for count in memo.values())
```

Explanation: We first iterate array $s$ to count the number of occurrence for each character. Then, we can simply iterate array $t$ to check whether they satisfy the requirement of an anagram. Finally, we need to check whether all of the number of occurrence for each character is zero.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

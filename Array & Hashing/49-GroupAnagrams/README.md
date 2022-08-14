# Group Anagrams

Problem can be found in [here](https://leetcode.com/problems/group-anagrams/)!

### [Solution](/Array%20%26%20Hashing/49-GroupAnagrams/solution.py): Sorting + Hash Table

```python
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    memo = defaultdict(list)
    for string in strs:
        sorted_string = "".join(sorted(string))
        memo[sorted_string].append(string)

    return memo.values()
```

Explanation: The key to cracking this problem is to acknowledge that A and B are a group of anagrams if and only if they are identical after their characters are sorted. For example, assume A = "eat" and B = "tea", they would be A = B = "aet" after sorted. Finally, we can use a hash table to look up if an anagram has already exists in O(1) time.

Time Complexity: ![O(n*mlongm)](<https://latex.codecogs.com/svg.image?\inline&space;O(n\cdot&space;mlogm)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of array $str$ and m is the maximum length of string in array $str$.

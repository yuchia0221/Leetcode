# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/contains-duplicate/)!

### [Solution](/Array%20%26%20Hashing/217-ContainsDuplicate/solution.py): Hash Table

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = set()
        for num in nums:
            if num in memo:
                return True
            memo.add(num)

        return False
```

Explanation: The strategy is to iterate the whole array once. In each iteration, we can use a hash table to memorize we have encountered this number. If we find out this number has already been seen, we know there must be a duplicated number in the list.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

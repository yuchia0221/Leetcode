# Two Sum

Problem can be found in [here](https://leetcode.com/problems/two-sum/)!

### [Solution](/Array%20%26%20Hashing/1-TwoSum/solution.py): Hash Table

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    memo = {}
    for index, num in enumerate(nums):
        try:
            return [memo[num], index]
        except KeyError:
            memo[target-num] = index
```

Explanation: We can solve this problem by iterating the array once. In each iteration, we can memorize the number needed for this number to add up to our target number by using hash map. When we find there is a match in our hash map, we can return the answer.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

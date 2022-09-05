# ubarray Sum Equals K

Problem can be found in [here](https://leetcode.com/problems/subarray-sum-equals-k/)!

### [Solution](/Prefix%20Sum/560-SubarraySumEqualsK/solution.py): Prefix Sum

```python
def subarraySum(nums: List[int], k: int) -> int:
    memo = defaultdict(int)
    current_sum = number = 0
    for num in nums:
        current_sum += num
        remaining = current_sum - k
        if current_sum == k:
            number += 1
        if remaining in memo:
            number += memo[remaining]

        memo[current_sum] += 1

    return number
```

Explanation: Basically, it is the same solution as [the problem](/Prefix%20Sum/560-SubarraySumEqualsK/) with little modifications.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

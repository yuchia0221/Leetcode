# Subarray Sums Divisible by K

Problem can be found in [here](https://leetcode.com/problems/subarray-sums-divisible-by-k/)!

### [Solution](/Prefix%20Sum/974-SubarraySumsDivisiblebyK/solution.py): Prefix Sum + Hash Table

```python
def subarraysDivByK(nums: List[int], k: int) -> int:
    prefix_sum = number_of_array = 0
    memo = defaultdict(int)
    memo[0] = 1

    for num in nums:
        prefix_sum = (prefix_sum + num) % k
        number_of_array += memo[prefix_sum]
        memo[prefix_sum] += 1

    return number_of_array
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

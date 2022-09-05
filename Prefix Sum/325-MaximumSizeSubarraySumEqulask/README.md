# Maximum Size Subarray Sum Equals k

Problem can be found in [here](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)!

### [Solution](/Prefix%20Sum/238-ProductofArrayExceptSelf/solution.py): Prefix Sum

```python
def maxSubArrayLen(nums: List[int], k: int) -> int:
    memo = defaultdict(int)
    current_sum = max_length = 0
    for i, num in enumerate(nums):
        current_sum += num
        remaining = current_sum - k
        if current_sum == k:
            max_length = i + 1
        elif remaining in memo:
            max_length = max(max_length, i-memo[remaining])

        if current_sum not in memo:
            memo[current_sum] = i

    return max_length
```

Explanation: To solve this problem in linear time, we can use the prefix sum technique. We need to iterate the whole array sequentially and memorize the subarray sum with a hash table. Suppose we have an array = [-2, 1, 2, -1, 1] and k = 3, we know that the length of the longest subarray sum equals k is 4 ([1, 2, -1, 1]). In the first iteration, the current sum is -2 and there is no -5 in the hash table (if there is one, we can discard the whole subarray starting from index 0 to i that sums up to 5 and get 3 by using subarray starting from index i+1 to current index). Therefore, we know we cannot make 3 with a subarray ending with this index and update the hash map to {-2: 0}. In the second iteration, the current sum is 1 and there is no 4 in the hash table. Therefore, we know we cannot make 3 with a subarray ending with this index and update the hash map to {-2: 0, -1: 1}. In the next iteration, the current sum is 1 and there is a -2 we need. We can update the longest length of subarray equals k.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

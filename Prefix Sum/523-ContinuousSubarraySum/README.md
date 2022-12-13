# Continuous Subarray Sum

Problem can be found in [here](https://leetcode.com/problems/continuous-subarray-sum/)!

### [Solution](/Prefix%20Sum/523-ContinuousSubarraySum/solution.py): Prefix Sum

```python
def checkSubarraySum(nums: List[int], k: int) -> bool:
    dic = {0: -1}
    prefix_sum = 0
    for i, number in enumerate(nums):
        prefix_sum = (prefix_sum + number) % k
        if prefix_sum not in dic:
            dic[prefix_sum] = i
        else:
            if i - dic[prefix_sum] >= 2:
                return True

    return False
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(min(n,k))](<https://latex.codecogs.com/svg.image?\inline&space;O(min(n,k))>)

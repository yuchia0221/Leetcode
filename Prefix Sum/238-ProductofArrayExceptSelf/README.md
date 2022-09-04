# Product of Array Except Self

Problem can be found in [here](https://leetcode.com/problems/product-of-array-except-self/)!

### [Solution](/Prefix%20Sum/238-ProductofArrayExceptSelf/solution.py): Prefix Sum

```python
def productExceptSelf(nums: List[int]) -> List[int]:
    prefix_sum = suffix_sum = 1
    output_list = [1] * len(nums)
    for i in range(len(nums)):
        output_list[i] *= prefix_sum
        output_list[-1-i] *= suffix_sum
        prefix_sum *= nums[i]
        suffix_sum *= nums[-1-i]

    return output_list
```

Explanation: Please refer to solution [here](https://github.com/yuchia0221/Grind-75/tree/main/Array/238-ProductofArrayExceptSelf)

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

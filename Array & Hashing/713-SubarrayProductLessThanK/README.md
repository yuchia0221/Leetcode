# Subarray Product Less Than K

Problem can be found in [here](https://leetcode.com/problems/subarray-product-less-than-k/)!

### [Solution](/Array%20%26%20Hashing/713-SubarrayProductLessThanK/solution.py): Sliding Windows

```python
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    product = 1
    left = number_of_subarray = 0
    for i, num in enumerate(nums):
        product *= num
        while product >= k:
            product /= nums[left]
            left += 1
        number_of_subarray += (i-left+1)

    return number_of_subarray
```

Explanation: By using the properties of the input: all of the elements in nums are larger or equal to 1, we can perform a sliding window to check if a subarray product is less than k. In each iteration, we multiply current num and run a while loop to find the smallest left index, which product ≤ k. We update the number of subarrays in this fashion as elaborated in the following example. Suppose we have variables nums=[10,5,2,6], left=0, right=2, and k=80. In this example, if we have left=0 and right=2, the current product is 100, which is larger than k. Therefore, we need to find the smallest left, which left+1 ≤ new_left ≤ right (left will become 1 in this case). As you can see, there are two subarrays that product is less than k: [5, 2] and [2].

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

# 4Sum

Problem can be found in [here](https://leetcode.com/problems/4sum/)!

### [Solution](/Hash%20Table/18-4Sum/solution.py): Hash Table + Sort

```python
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
        result = []

        # If we have run out of numbers to add, return result
        if not nums:
            return result

        # If the smallest value multiplies by k is larger than target or
        # the largest value multiplies by k is larger than target,
        # meaning that we cannot make target with a combination in nums.
        if nums[0] * k > target or nums[-1] * k < target:
            return result

        # Solve this problem as a two sum problem
        if k == 2:
            return twoSum(nums, target)
        else:
            for i in range(len(nums)):
                # To pass duplicated solutions
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i+1:], target-nums[i], k-1):
                        result.append([nums[i]] + subset)

            return result

    def twoSum(nums: List[int], target: int) -> List[List[int]]:
        result = []
        memo = set()
        for i in range(len(nums)):
            # To pass duplicated solutions
            if len(result) == 0 or result[-1][1] != nums[i]:
                if target - nums[i] in memo:
                    result.append([target-nums[i], nums[i]])

            memo.add(nums[i])

        return result
```

Explanation: We can first sort nums and sequentially simplify this problem into a two sum problem.

Time Complexity: ![O(n^{k−1})](<https://latex.codecogs.com/svg.image?\inline&space;O(n^{k−1})>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

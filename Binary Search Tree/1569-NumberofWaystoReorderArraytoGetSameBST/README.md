# Number of Ways to Reorder Array to Get Same BST

Problem can be found in [here](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)!

### [Solution](/Binary%20Search%20Tree/1569-NumberofWaystoReorderArraytoGetSameBST/solution.py): Recursion

```python
def numOfWays(nums: List[int]) -> int:
    def dfs(nums: List[int]) -> int:
        if len(nums) < 3:
            return 1

        left_nodes = [number for number in nums if number < nums[0]]
        right_nodes = [number for number in nums if number > nums[0]]
        return dfs(left_nodes) * dfs(right_nodes) * comb(len(nums) - 1, len(left_nodes)) % module

    module = pow(10, 9) + 7
    return (dfs(nums) - 1) % module
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

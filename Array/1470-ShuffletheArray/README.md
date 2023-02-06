# Shuffle the Array

Problem can be found in [here](https://leetcode.com/problems/shuffle-the-array/)!

### [Solution](/Array/1470-ShuffletheArray/solution.py)

```python
def shuffle(nums: List[int], n: int) -> List[int]:
    output_list = []

    for i in range(n):
        output_list.append(nums[i])
        output_list.append(nums[i+n])

    return output_list
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

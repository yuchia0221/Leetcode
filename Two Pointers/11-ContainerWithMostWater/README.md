# Container With Most Water

Problem can be found in [here](https://leetcode.com/problems/container-with-most-water/)!

### [Solution](/Two%20Pointers/11-ContainerWithMostWater/solution.py): Two Pointers

```python
def maxArea(heights: List[int]) -> int:
    max_volumne = 0
    left, right = 0, len(heights)-1
    while left < right:
        height, width = min(heights[left], heights[right]), right-left
        max_volumne = max(max_volumne, height*width)
        if heights[left] >= heights[right]:
            while left < right and height >= height[right]:
                right -= 1
        else:
            while left < right and height >= height[left]:
                left += 1

    return max_volumne
```

Explanation: Please refer to [link](https://github.com/yuchia0221/Grind-75/tree/main/Array/11-ContainerWithMostWater) for explanation.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

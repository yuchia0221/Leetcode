# Trapping Rain Water

Problem can be found in [here](https://leetcode.com/problems/trapping-rain-water/)!

### [Solution](/Two%20Pointers/42-TrappingRainWater/solution.py): Monotonic Stack

```python
def trap(heights: List[int]) -> int:
    area = 0
    stack = []
    for i in range(len(heights)):
        while stack and heights[stack[-1]] < heights[i]:
            candidate = heights[stack.pop()]
            if stack:
                height = min(heights[i], heights[stack[-1]]) - candidate
                width = i - stack[-1] - 1
                area += height * width
        stack.append(i)

    return area
```

Explanation: Please refer to [link](https://github.com/yuchia0221/Grind-75/tree/main/Stack/42-TrappingRainWater) for explanation.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

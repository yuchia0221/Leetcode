# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

Problem can be found in [here](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)!

### [Solution](/Array/215-KthLargestElementinanArray/solution.py): Quick Select

```python
def maxArea(h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    horizontalCuts.sort()
    verticalCuts.sort()

    max_width = max(verticalCuts[0], w-verticalCuts[-1])
    max_height = max(horizontalCuts[0], h-horizontalCuts[-1])
    for i in range(1, len(horizontalCuts)):
        max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i-1])
    for i in range(1, len(verticalCuts)):
        max_width = max(max_width, verticalCuts[i] - verticalCuts[i-1])

    return (max_width * max_height) % (pow(10, 9) + 7)
```

Time Complexity: ![O(nlogn+mlogm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn+mlogm)>), Space Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+m)>), where n and m is the length of horizontalCuts and verticalCuts, respecitvely.

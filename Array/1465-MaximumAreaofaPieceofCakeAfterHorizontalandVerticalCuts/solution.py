from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        max_width = max(verticalCuts[0], w-verticalCuts[-1])
        max_height = max(horizontalCuts[0], h-horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i-1])

        return (max_width * max_height) % (pow(10, 9) + 7)

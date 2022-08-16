from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
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

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
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

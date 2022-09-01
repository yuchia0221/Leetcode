from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        output_list = []
        for i, num in enumerate(nums):
            while queue and num >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            if queue[0] == i-k:
                queue.popleft()
            if i >= k - 1:
                output_list.append(nums[queue[0]])

        return output_list

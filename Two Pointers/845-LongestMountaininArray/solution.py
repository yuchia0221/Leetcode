from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_length, peak = 0, 1
        while peak < len(arr)-1:
            if arr[peak] > arr[peak-1] and arr[peak] > arr[peak+1]:
                left, right = peak-1, peak+1
                while left > 0 and arr[left] > arr[left-1]:
                    left -= 1
                while right < len(arr)-1 and arr[right] > arr[right+1]:
                    right += 1
                max_length = max(max_length, right-left+1)
                peak = right + 1
            else:
                peak += 1

        return max_length

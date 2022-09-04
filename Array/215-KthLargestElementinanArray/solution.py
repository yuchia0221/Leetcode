from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(left: int, right: int):
            pivot_value, index = nums[right], left
            for i in range(left, right):
                if nums[i] <= pivot_value:
                    nums[index], nums[i] = nums[i], nums[index]
                    index += 1

            nums[index], nums[right] = nums[right], nums[index]
            if index == k:
                return nums[index]
            elif index > k:
                return quick_select(left, index-1)
            else:
                return quick_select(index+1, right)

        k = len(nums)-k
        return quick_select(0, len(nums)-1)

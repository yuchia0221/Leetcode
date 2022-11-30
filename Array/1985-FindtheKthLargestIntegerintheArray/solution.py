from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def parition(left: int, right: int) -> int:
            pivot = nums[right]
            j = left

            for i in range(left, right):
                if int(nums[i]) <= int(pivot):
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1

            nums[j], nums[right] = nums[right], nums[j]
            return j

        def quick_select(left: int, right: int, k: int) -> str:
            if left == right:
                return nums[left]

            index = parition(left, right)
            if index == k:
                return nums[index]
            elif index > k:
                return quick_select(left, index-1, k)
            else:
                return quick_select(index+1, right, k)

        return quick_select(0, len(nums)-1, len(nums)-k)

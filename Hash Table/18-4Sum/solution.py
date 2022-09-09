from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            result = []

            if not nums:
                return result

            if nums[0] * k > target and nums[-1] * k < target:
                return result

            if k == 2:
                return twoSum(nums, target)
            else:
                for i in range(len(nums)):
                    if i == 0 or nums[i-1] != nums[i]:
                        for subset in kSum(nums[i+1:], target-nums[i], k-1):
                            result.append([nums[i]] + subset)

                return result

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            memo = set()
            for i in range(len(nums)):
                if len(result) == 0 or result[-1][1] != nums[i]:
                    if target - nums[i] in memo:
                        result.append([target-nums[i], nums[i]])

                memo.add(nums[i])

            return result

        nums.sort()
        return kSum(nums, target, 4)

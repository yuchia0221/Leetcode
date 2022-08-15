from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            current_value = numbers[left] + numbers[right]
            if current_value == target:
                break
            elif current_value < target:
                left += 1
            else:
                right -= 1

        return [left+1, right+1]

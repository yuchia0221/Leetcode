from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def count_division_sum(speed: int) -> int:
            times = 0
            for num in nums:
                counter, remainder = num // speed, num % speed
                if remainder:
                    counter += 1
                times += counter

            return times

        start, end = 1, max(nums)
        while start < end:
            k = (start+end) // 2
            if count_division_sum(k) <= threshold:
                end = k
            else:
                start = k + 1

        return start

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finish_bananas_time(speed: int) -> int:
            time = 0
            for pile in piles:
                counter, remainder = pile // speed, pile % speed
                if remainder:
                    counter += 1
                time += counter

            return time

        start, end = 1, max(piles)
        while start < end:
            k = (start+end) // 2
            if finish_bananas_time(k) <= h:
                end = k
            else:
                start = k + 1

        return start


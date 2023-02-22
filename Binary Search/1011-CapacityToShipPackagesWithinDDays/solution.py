from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            current_weight, ship_days = 0, 1
            for weight in weights:
                if current_weight + weight > mid:
                    current_weight = 0
                    ship_days += 1
                current_weight += weight

            if ship_days > days:
                left = mid + 1
            else:
                right = mid

        return left

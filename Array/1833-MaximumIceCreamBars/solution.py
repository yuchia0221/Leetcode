from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        index = 0
        costs.sort()

        while coins >= 0 and index < len(costs):
            if costs[index] <= coins:
                coins -= costs[index]
                index += 1
            else:
                break

        return index

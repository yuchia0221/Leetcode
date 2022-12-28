from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remainings = sorted(map(lambda x, y: x-y, capacity, rocks))

        full_bags_num = 0
        for remain in remainings:
            if remain <= additionalRocks:
                additionalRocks -= remain
                full_bags_num += 1
            else:
                break

        return full_bags_num

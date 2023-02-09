from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        basket = defaultdict(int)

        for right in range(len(fruits)):
            basket[fruits[right]] += 1

            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

        return len(fruits) - left

from bisect import bisect_left
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result, prefix, i = [], '', 0

        for char in searchWord:
            prefix += char
            i = bisect_left(products, prefix, i)
            result.append([w for w in products[i:i + 3] if w.startswith(prefix)])

        return result

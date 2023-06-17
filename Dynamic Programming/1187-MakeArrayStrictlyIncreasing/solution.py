from functools import cache
from typing import List
from bisect import bisect_right


def makeArrayIncreasing(arr1: List[int], arr2: List[int]) -> int:
    @cache
    def get_minimum_operations(index: int, previous_value: int) -> int:
        if index == len(arr1):
            return 0

        current_cost = float("inf")
        if arr1[index] > previous_value:
            current_cost = get_minimum_operations(index+1, arr1[index])

        new_index = bisect_right(arr2, previous_value)
        if new_index < len(arr2):
            current_cost = min(current_cost, 1 + get_minimum_operations(index+1, arr2[new_index]))

        return current_cost

    arr2.sort()
    minimum_operations = get_minimum_operations(0, -1)
    return minimum_operations if minimum_operations != float("inf") else -1

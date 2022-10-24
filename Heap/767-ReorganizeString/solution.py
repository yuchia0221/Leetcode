from collections import Counter
from heapq import heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        for word, times in counter.items():
            heappush(heap, (-times, word))

        result = []
        while heap:
            largest_times, largest_char = heappop(heap)
            if result and result[-1] == largest_char:
                if not heap:
                    return ""
                second_times, second_char = heappop(heap)
                result.append(second_char)
                new_times = second_times+1
                if new_times != 0:
                    heappush(heap, (new_times, second_char))
                heappush(heap, (largest_times, largest_char))
            else:
                result.append(largest_char)
                new_times = largest_times+1
                if new_times != 0:
                    heappush(heap, (new_times, largest_char))

        return "".join(result)

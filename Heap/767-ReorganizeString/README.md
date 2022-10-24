# Reorganize String

Problem can be found in [here](https://leetcode.com/problems/reorganize-string/)!

### [Solution](/Heap/767-ReorganizeString/solution.py): Heap

```python
def reorganizeString(s: str) -> str:
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
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of the buildings array.

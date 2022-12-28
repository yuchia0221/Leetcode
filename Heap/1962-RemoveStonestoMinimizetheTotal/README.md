# Remove Stones to Minimize the Total

Problem can be found in [here](https://leetcode.com/problems/remove-stones-to-minimize-the-total/)!

### [Solution](/Heap/1962-RemoveStonestoMinimizetheTotal/solution.py): Heap

```python
def minStoneSum(piles: List[int], k: int) -> int:
    heap = [-pile for pile in piles]
    heapify(heap)

    for _ in range(k):
        pile = -heappop(heap)
        heappush(heap, -math.ceil(pile/2))

    return -sum(heap)
```

Time Complexity: ![O(klogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(klogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

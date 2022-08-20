# Koko Eating Bananas

Problem can be found in [here](https://leetcode.com/problems/koko-eating-bananas/)!

### [Solution](/Binary%20Search/875-KokoEatingBananas/solution.py): Binary Search

```python
def minEatingSpeed(piles: List[int], h: int) -> int:
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
```

Explanaiton: We can perform binary search to find the minimum k such that it can be eaten in h hours. After an iteration, we can remove half of the searching range. To calculate the time needed to finish all banana piles is fairly easy, we can simply iterate the whole array, compute the time for it to consume for each pile, and add them up. This algorithm is correct because the following condition as the problem suggested.

> If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Time Complexity: ![O(nlogm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogm)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n is the number of piles and m is the maximum number of bananas in piles.

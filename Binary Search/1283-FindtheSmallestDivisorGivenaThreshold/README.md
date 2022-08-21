# Find the Smallest Divisor Given a Threshold

Problem can be found in [here](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)!

### [Solution](/Binary%20Search/1283-FindtheSmallestDivisorGivenaThreshold/solution.py): Binary Search

```python
def smallestDivisor(nums: List[int], threshold: int) -> int:
    def count_division_sum(speed: int) -> int:
        times = 0
        for num in nums:
            counter, remainder = num // speed, num % speed
            if remainder:
                counter += 1
            times += counter

        return times

    start, end = 1, max(nums)
    while start < end:
        k = (start+end) // 2
        if count_division_sum(k) <= threshold:
            end = k
        else:
            start = k + 1

    return start
```

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n is the length of array nums and m is the maximum number of bananas in piles.

# Pairs of Songs With Total Durations Divisible by 60

Problem can be found in [here](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)!

### [Solution](/Hash%20Table/1010-PairsofSongsWithTotalDurationsDivisibleby60/solution.py): Hash Table

```python
def numPairsDivisibleBy60(songs: List[int]) -> int:
    remainders = defaultdict(int)
    number_of_pairs, divisor = 0, 60

    for time in songs:
        if time % divisor == 0:
            number_of_pairs += remainders[0]
        else:
            number_of_pairs += remainders[divisor-time % divisor]
        remainders[time % divisor] += 1

    return number_of_pairs
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

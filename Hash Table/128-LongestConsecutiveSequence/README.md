# Longest Consecutive Sequence

Problem can be found in [here](https://leetcode.com/problems/longest-consecutive-sequence/)!

### [Solution1](/Hash%20Table/128-LongestConsecutiveSequence/solution1.py): Disjoint Set

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

### [Solution2](/Hash%20Table/128-LongestConsecutiveSequence/solution2.py): Hash Table

The solution is from [leetcode](https://leetcode.com/problems/longest-consecutive-sequence/solution/).

```python
def longestConsecutive(nums: List[int]) -> int:
    longest_sequence = 0
    number_set = set(nums)

    for num in number_set:
        if num-1 not in number_set:
            current_num = num
            current_streak = 1

            while current_num+1 in number_set:
                current_num += 1
                current_streak += 1

            longest_sequence = max(longest_sequence, current_streak)

    return longest_sequence
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

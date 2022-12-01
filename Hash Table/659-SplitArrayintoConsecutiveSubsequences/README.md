# Split Array into Consecutive Subsequences

Problem can be found in [here](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)!

### [Solution](/Hash%20Table/659-SplitArrayintoConsecutiveSubsequences/solution.py): Hash Table

```python
def isPossible(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    frequency = Counter(nums)
    subsequence = defaultdict(int)
    for num in nums:
        if frequency[num] == 0:
            continue

        frequency[num] -= 1
        if subsequence[num-1] > 0:
            subsequence[num-1] -= 1
            subsequence[num] += 1
        elif frequency[num+1] and frequency[num+2]:
            frequency[num+1] -= 1
            frequency[num+2] -= 1
            subsequence[num+2] += 1
        else:
            return False

    return True
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

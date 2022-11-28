# Find Players With Zero or One Losses]

Problem can be found in [here](https://leetcode.com/problems/find-players-with-zero-or-one-losses/)!

### [Solution](/Array/2225-FindPlayersWithZeroorOneLosses/solution.py): Counting Sort

```python
def findWinners(matches: List[List[int]]) -> List[List[int]]:
    losses = [-1] * 100001

    for winner, loser in matches:
        if losses[winner] == -1:
            losses[winner] = 0
        if losses[loser] == -1:
            losses[loser] = 1
        else:
            losses[loser] += 1

    answer = [[], []]
    for index, loss in enumerate(losses):
        if loss == 0:
            answer[0].append(index)
        elif loss == 1:
            answer[1].append(index)

    return answer
```

Time Complexity: ![O(n+k)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+k)>), Space Complexity: ![O(k)](<https://latex.codecogs.com/svg.image?\inline&space;O(k)>), where n is the size of the input array matches, and k is the range of values in winner or loser.

# Partition Labels

Problem can be found in [here](https://leetcode.com/problems/partition-labels/)!

### [Solution](/String/763-PartitionLabels/solution.py): Greedy

```python
def partitionLabels(s: str) -> List[int]:
    answer = []
    end_position = last_position = 0
    memo = {char: index for index, char in enumerate(s)}

    for index, char in enumerate(s):
        end_position = max(end_position, memo[char])
        if index == end_position:
            answer.append(index-last_position+1)
            last_position = index + 1

    return answer
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

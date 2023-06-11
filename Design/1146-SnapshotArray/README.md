# Snapshot Array

Problem can be found in [here](https://leetcode.com/problems/snapshot-array/)!

### [Solution](/Design/1146-SnapshotArray/solution.py)

```python
class SnapshotArray:
    def __init__(self, length: int):
        self.snapshots = 0
        self.max_value = pow(10, 9)
        self.records = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.records[index].append([self.snapshots, val])

    def snap(self) -> int:
        self.snapshots += 1
        return self.snapshots - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect_right(self.records[index], [snap_id, self.max_value])
        return self.records[index][snap_index-1][1]
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the maximum number of calls.

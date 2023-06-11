from bisect import bisect_right


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

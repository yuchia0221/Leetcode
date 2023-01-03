from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted_columns = 0

        for column in zip(*strs):
            for i in range(1, len(column)):
                if column[i-1] > column[i]:
                    deleted_columns += 1
                    break

        return deleted_columns

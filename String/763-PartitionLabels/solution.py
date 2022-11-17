from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        answer = []
        end_position = last_position = 0
        memo = {char: index for index, char in enumerate(s)}

        for index, char in enumerate(s):
            end_position = max(end_position, memo[char])
            if index == end_position:
                answer.append(index-last_position+1)
                last_position = index + 1

        return answer

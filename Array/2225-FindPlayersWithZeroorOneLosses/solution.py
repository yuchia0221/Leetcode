from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
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
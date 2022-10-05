from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output_list = []
        candidates = sorted(candidates)
        self.dfs(candidates, 0, target, [], output_list)
        return output_list

    def dfs(self, nums: List[int], index: int, target: int, tempt: List[int], answer: List[List[int]]) -> None:
        if target < 0:
            return
        elif target == 0:
            answer.append(list(tempt))
            return

        for i in range(index, len(nums)):
            if i > index and nums[i-1] == nums[i]:
                continue
            else:
                tempt.append(nums[i])
                self.dfs(nums, i+1, target-nums[i], tempt, answer)
                tempt.pop()

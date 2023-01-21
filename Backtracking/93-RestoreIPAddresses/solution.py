from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(start: int, candidate: List[str]) -> None:
            if start == len(s):
                if len(candidate) == 4:
                    result.append(".".join(candidate))
                return

            if s[start] == "0":
                dfs(start+1, candidate+["0"])
                return

            for end in range(start+1, min(start+4, len(s)+1)):
                address = s[start:end]
                if 0 <= int(address) <= 255:
                    dfs(end, candidate+[address])

        result = []
        dfs(0, [])
        return result

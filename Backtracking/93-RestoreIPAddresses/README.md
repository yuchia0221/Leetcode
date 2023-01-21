# Restore IP Addresses

Problem can be found in [here](https://leetcode.com/problems/restore-ip-addresses/)!

### [Solution](/Backtracking/93-RestoreIPAddresses/solution.py): Backtracking

```python
def restoreIpAddresses(s: str) -> List[str]:
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
```

Time Complexity: ![O(m^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m^n)>), Space Complexity: ![O(m*n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m*n)>), where n is the number of splits and m is the digits of each integer.

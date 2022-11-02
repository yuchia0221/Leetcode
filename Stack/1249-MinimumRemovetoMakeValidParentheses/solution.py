class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        string = list(s)
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            elif char == ")":
                if not stack or s[stack[-1]] != "(":
                    string[index] = ""
                else:
                    stack.pop()

            else:
                continue

        while stack:
            string[stack.pop()] = ""

        return "".join(string)

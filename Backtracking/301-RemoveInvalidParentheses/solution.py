from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def helper(expression: List[str], index: int, open_count: int, close_count: int, open_remove: int, close_remove: int):
            if index == len(s):
                if open_remove == 0 and close_remove == 0:
                    result.add("".join(expression))
            else:
                current_char = s[index]
                if current_char == "(" and open_remove > 0:
                    helper(expression[:], index+1, open_count, close_count, open_remove-1, close_remove)
                elif current_char == ")" and close_remove > 0:
                    helper(expression[:], index+1, open_count, close_count, open_remove, close_remove-1)

                if current_char != "(" and current_char != ")":
                    helper(expression+[current_char], index+1, open_count, close_count, open_remove, close_remove)
                elif current_char == "(":
                    helper(expression+[current_char], index+1, open_count+1, close_count, open_remove, close_remove)
                elif current_char == ")" and open_count > close_count:
                    helper(expression+[current_char], index+1, open_count, close_count+1, open_remove, close_remove)

        result = set()
        open_remove = close_remove = 0
        for char in s:
            if char == "(":
                open_remove += 1
            elif char == ")":
                if open_remove == 0:
                    close_remove += 1
                else:
                    open_remove -= 1

        helper([], 0, 0, 0, open_remove, close_remove)
        return list(result)

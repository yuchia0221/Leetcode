from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(s_index: int, p_index: int) -> bool:
            if p_index == len(p):
                return s_index == len(s)
            else:
                is_current_char_match = s_index < len(s) and p[p_index] in set([s[s_index], "."])
                if p_index+1 < len(p) and p[p_index+1] == "*":
                    return dp(s_index, p_index+2) or is_current_char_match and dp(s_index+1, p_index)
                else:
                    return is_current_char_match and dp(s_index+1, p_index+1)

        return dp(0, 0)

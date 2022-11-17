class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        string = list(palindrome)
        for index in range(len(string) // 2):
            if string[index] != "a":
                string[index] = "a"
                break
        else:
            string[-1] = "b"

        return "".join(string)

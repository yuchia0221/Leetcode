class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(string: str):
            return string == string[::-1]

        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                delete_left, delete_right = s[left+1:right+1], s[left:right]
                return isPalindrome(delete_left) or isPalindrome(delete_right)

            left += 1
            right -= 1

        return True

from typing import List


from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0
        while right < len(chars):
            counter = 1
            chars[left] = chars[right]
            while right < len(chars)-1 and chars[right] == chars[right+1]:
                right += 1
                counter += 1

            if counter > 1:
                for digit in str(counter):
                    left += 1
                    chars[left] = digit

            left += 1
            right += 1

        return left

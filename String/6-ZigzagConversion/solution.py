class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zipzag_string = ""
        cycle = 2*numRows - 2
        for i in range(numRows):
            for j in range(0, len(s), cycle):
                if i + j >= len(s):
                    break
                zipzag_string += s[i + j]
                if (i != 0 and i != numRows-1 and j+cycle-i < len(s)):
                    zipzag_string += s[j+cycle-i]

        return zipzag_string

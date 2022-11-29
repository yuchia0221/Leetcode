from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """ Encodes a list of strings to a single string """
        encoded_string = ""
        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """ Decodes a single string to a list of strings """
        index = 0
        decoded_string = []
        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            length = int(s[index:j])
            decoded_string.append(s[j+1:j+1+length])
            index = j + 1 + length

        return decoded_string

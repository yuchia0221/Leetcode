class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        available_slot = 1
        for char in preorder.split(","):
            available_slot -= 1
            if available_slot < 0:
                return False
            if char != "#":
                available_slot += 2

        return available_slot == 0

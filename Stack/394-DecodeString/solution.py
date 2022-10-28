class Solution(object):
    def decodeString(self, s):
        stack = []
        current_number = 0
        current_string = ""
        for char in s:
            if char == "[":
                stack.append(current_string)
                stack.append(current_number)
                current_number, current_string = 0, ""
            elif char == "]":
                num = stack.pop()
                prevString = stack.pop()
                current_string = prevString + num*current_string
            elif char.isdigit():
                current_number = current_number*10 + int(char)
            else:
                current_string += char
                
        return current_string

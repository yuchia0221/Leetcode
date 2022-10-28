class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        prev_operator = "+"
        s += "+"
        stack = []
        for char in s:
            if char.isdigit():
                number = number*10 + int(char)
            elif char == " ":
                continue
            else:
                if prev_operator == "+":
                    stack.append(number)
                elif prev_operator == "-":
                    stack.append(-number)
                elif prev_operator == "*":
                    stack.append(number * stack.pop())
                else:
                    stack.append(int(stack.pop() / number))

                number, prev_operator = 0, char

        return sum(stack)

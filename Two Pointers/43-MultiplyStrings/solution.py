class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        for i in range(len(num1)-1, -1, -1):
            base = pow(10, len(num1)-i-1)
            for j in range(len(num2)-1, -1, -1):
                result += int(num1[i]) * int(num2[j]) * base
                base *= 10

        return str(result)

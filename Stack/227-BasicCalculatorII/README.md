# Basic Calculator II

Problem can be found in [here](https://leetcode.com/problems/basic-calculator-ii/)!

### [Solution](/Stack/227-BasicCalculatorII/solution.py): Stack

```python
def calculate(s: str) -> int:
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

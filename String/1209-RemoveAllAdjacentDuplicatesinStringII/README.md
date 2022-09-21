# Remove All Adjacent Duplicates in String II

Problem can be found in [here](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)!

### [Solution](/String/5-LongestPalindromicSubstring/solution.py)

```python
@dataclass
class StackNode:
    char: str
    counter: int



def removeDuplicates(s: str, k: int) -> str:
    stack = []
    for char in s:
        if stack and stack[-1].char == char:
            stack[-1].counter += 1
        else:
            stack.append(StackNode(char, 1))

        if stack[-1].counter == k:
            stack.pop()

    output_string = ""
    for stack_node in stack:
        output_string += stack_node.char * stack_node.counter

    return output_string
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

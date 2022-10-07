# Remove Invalid Parentheses

Problem can be found in [here](https://leetcode.com/problems/remove-invalid-parentheses/)!

### [Solution](/Backtracking/301-RemoveInvalidParentheses/solution.py): Backtracking

```python
def removeInvalidParentheses(s: str) -> List[str]:
    def helper(expression: List[str], index: int, open_count: int, close_count: int, open_remove: int, close_remove: int):
        if index == len(s):
            if open_remove == 0 and close_remove == 0:
                result.add("".join(expression))
        else:
            current_char = s[index]
            if current_char == "(" and open_remove > 0:
                helper(expression[:], index+1, open_count, close_count, open_remove-1, close_remove)
            elif current_char == ")" and close_remove > 0:
                helper(expression[:], index+1, open_count, close_count, open_remove, close_remove-1)

            if current_char != "(" and current_char != ")":
                helper(expression+[current_char], index+1, open_count, close_count, open_remove, close_remove)
            elif current_char == "(":
                helper(expression+[current_char], index+1, open_count+1, close_count, open_remove, close_remove)
            elif current_char == ")" and open_count > close_count:
                helper(expression+[current_char], index+1, open_count, close_count+1, open_remove, close_remove)

    result = set()
    open_remove = close_remove = 0
    for char in s:
        if char == "(":
            open_remove += 1
        elif char == ")":
            if open_remove == 0:
                close_remove += 1
            else:
                open_remove -= 1

    helper([], 0, 0, 0, open_remove, close_remove)
    return list(result)
```

Explanation: We can first perform a one-pass search to count how many misplace parentheses in the string. By doing so, we know how many parentheses we need to remove to improve the time complexity. For each backtracking, we need to first determine we reach the end and the string so far is valid or not (just check if `open_count = 0` and `close_count = 0`). If so, we can just append it into our answer list (use set to handle duplicated answers). If we have not reached the end, we have at most two operations to perform. One is to remove this parenthesis and the other is to keep it. In the first case, if we want to remove it, we have to first check whether we can remove this parenthesis. Notice that if current character is “)” we need to check whether the number of “(” we met so far is larger than the number of “)” to keep it in the other case since if we met # of ( > # of ), there is nothing we can do further to make the string become valid again (think about `(()`).

Time Complexity: ![O(2^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(2^n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of the string.

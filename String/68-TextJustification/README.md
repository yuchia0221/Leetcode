# Text Justification

Problem can be found in [here](https://leetcode.com/problems/text-justification/)!

### [Solution](/String/68-TextJustification/solution.py)

```python
def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    current_line_length = 0
    current_line, new_lines = [], []
    for i in range(len(words)):
        if current_line_length + len(current_line) + len(words[i]) <= maxWidth:
            current_line.append(words[i])
            current_line_length += len(words[i])
            continue
        else:
            if len(current_line) == 1:
                new_lines.append(current_line[0].ljust(maxWidth))
            else:
                spaces = (maxWidth-current_line_length) // (len(current_line)-1)
                extra_spaces = (maxWidth-current_line_length) % (len(current_line)-1)
                for j in range(len(current_line)-1):
                    if extra_spaces > 0:
                        current_line[j] += " " * (spaces+1)
                        extra_spaces -= 1
                    else:
                        current_line[j] += " " * spaces

                new_lines.append("".join(current_line))
            current_line, current_line_length = [words[i]], len(words[i])

    new_lines.append(" ".join(current_line).ljust(maxWidth))
    return new_lines
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

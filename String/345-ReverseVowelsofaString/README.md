# Reverse Vowels of a String

Problem can be found in [here](https://leetcode.com/problems/reverse-vowels-of-a-string/)!

### [Solution](/String/345-ReverseVowelsofaString/solution.py): Two Pointers

```python
def reverseVowels(s: str) -> str:
    s = list(s)
    vowels = set("aeiouAEIOU")
    left, right = 0, len(s)-1
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        else:
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1

    return "".join(s)
```

Explanation: We can apply two pointers to solve this problem. One pointer starts form the left end of a string and the other starts from the right end of that. In each iteration, if we find that more than one is not vowels, then we update the index := index+1. Until we reach both of them are vowels, we perform a swap operation.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

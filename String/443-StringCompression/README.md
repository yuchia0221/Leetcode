# String Compression

Problem can be found in [here](https://leetcode.com/problems/string-compression/)!

### [Solution](/String/68-TextJustification/solution.py): Two pointers

```python
def compress(chars: List[str]) -> int:
    left = right = 0
    while right < len(chars):
        counter = 1
        chars[left] = chars[right]
        while right < len(chars)-1 and chars[right] == chars[right+1]:
            right += 1
            counter += 1

        if counter > 1:
            for digit in str(counter):
                left += 1
                chars[left] = digit

        left += 1
        right += 1

    return left
```

Explanation: We can use left and right pointers to solve this problem in one pass. The left pointer indicates which position we should store the compressed data, while the right pointer will keep searching for consecutive duplicated characters.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

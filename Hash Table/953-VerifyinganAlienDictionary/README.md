# Verifying an Alien Dictionary

Problem can be found in [here](https://leetcode.com/problems/verifying-an-alien-dictionary/)!

### [Solution](/Hash%20Table/953-VerifyinganAlienDictionary/solution.py): Hash Table

```python
def isAlienSorted(words: List[str], order: str) -> bool:
    char_order = dict()
    for index, char in enumerate(order):
        char_order[char] = index

    for i in range(1, len(words)):
        previous_word, current_word = words[i-1], words[i]
        for char1, char2 in zip(previous_word, current_word):
            if char_order[char1] > char_order[char2]:
                return False
            elif char_order[char1] < char_order[char2]:
                break
        else:
            if len(previous_word) > len(current_word):
                return False

    return True
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

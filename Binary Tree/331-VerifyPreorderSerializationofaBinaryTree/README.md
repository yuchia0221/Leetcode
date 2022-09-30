# Verify Preorder Serialization of a Binary Tree

Problem can be found in [here](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/)!

### [Solution](/Binary%20Tree/331-VerifyPreorderSerializationofaBinaryTree/solution.py)

```python
def isValidSerialization(preorder: str) -> bool:
    available_slot = 1
    for char in preorder.split(","):
        available_slot -= 1
        if available_slot < 0:
            return False
        if char != "#":
            available_slot += 2

    return available_slot == 0
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

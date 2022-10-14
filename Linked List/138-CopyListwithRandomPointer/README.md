# Copy List with Random Pointer

Problem can be found in [here](https://leetcode.com/problems/copy-list-with-random-pointer/)!

```python
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
```

### [Solution](/Linked%20List/138-CopyListwithRandomPointer/solution.py)

```python
class Solution:
    def cloned_node(self, node: "Optional[Node]") -> "Optional[Node]":
        if not node:
            return None
        try:
            return self.visted_node[node]
        except KeyError:
            self.visted_node[node] = Node(node.val)
            return self.visted_node[node]

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        self.visted_node = {}
        dummy_head = head
        new_head = Node(head.val)
        self.visted_node[head] = new_head
        while head:
            new_head.next = self.cloned_node(head.next)
            new_head.random = self.cloned_node(head.random)
            head, new_head = head.next, new_head.next

        return self.visted_node[dummy_head]
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>).

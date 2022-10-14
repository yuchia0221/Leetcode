# Reverse Linked List II

Problem can be found in [here](https://leetcode.com/problems/reverse-linked-list-ii/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/92-ReverseLinkedListII/solution.py)

```python
def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if left == right:
        return head

    previous_head = dummy_node = ListNode(0, head)
    for _ in range(left-1):
        previous_head = previous_head.next

    previous_node = None
    current_node = previous_head.next
    for _ in range(right-left+1):
        next_node = current_node.next
        current_node.next = previous_node
        previous_node, current_node = current_node, next_node

    previous_head.next.next = current_node
    previous_head.next = previous_node

    return dummy_node.next
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

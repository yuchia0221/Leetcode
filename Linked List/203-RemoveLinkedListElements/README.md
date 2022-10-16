# Remove Linked List Elements

Problem can be found in [here](https://leetcode.com/problems/remove-linked-list-elements/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/203-RemoveLinkedListElements/solution.py): Two Pointers

```python
def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return head

    dummy_head = previous_node = ListNode(0, head)
    while head:
        if head.val != val:
            previous_node = head
        else:
            previous_node.next = head.next
        head = head.next

    return dummy_head.next
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

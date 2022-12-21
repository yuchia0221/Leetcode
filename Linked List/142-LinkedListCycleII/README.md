# Linked List Cycle II

Problem can be found in [here](https://leetcode.com/problems/linked-list-cycle-ii/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/142-LinkedListCycleII/solution.py): Two Pointers

```python
def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    intersection = get_intersect(head)
    if intersection == None:
        return None

    pointer1, pointer2 = head, intersection
    while pointer1 != pointer2:
        pointer1, pointer2 = pointer1.next, pointer2.next

    return pointer1

def get_intersect(head: ListNode) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow

    return None
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

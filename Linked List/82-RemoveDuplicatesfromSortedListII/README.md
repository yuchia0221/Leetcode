# Remove Duplicates from Sorted List II

Problem can be found in [here](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/82-RemoveDuplicatesfromSortedListII/solution.py): Two Pointers

```python
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    previous_node = dummy_head = ListNode(0, head)
    while head:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            previous_node.next = head.next
        else:
            previous_node = previous_node.next
        head = head.next

    return dummy_head.next
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

# Partition List

Problem can be found in [here](https://leetcode.com/problems/partition-list/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/86-PartitionList/solution.py): Two Pointers

```python
def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    dummy_after = after = ListNode()
    dummy_before = before = ListNode()

    while head:
        # If the original list node is lesser than the given x,
        # assign it to the before list.
        if head.val < x:
            before.next = head
            before = before.next
        else:
        # If the original list node is greater or equal to the given x,
        # assign it to the after list.
            after.next = head
            after = after.next
        head = head.next

    # Last node of "after" list would also be ending node of the reformed list
    after.next = None
    # Once all the nodes are correctly assigned to the two lists,
    # combine them to form a single list which would be returned.
    before.next = dummy_after.next
    return dummy_before.next
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

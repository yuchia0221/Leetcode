# Odd Even Linked List

Problem can be found in [here](https://leetcode.com/problems/odd-even-linked-list/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/328-OddEvenLinkedList/solution.py): Two Pointers

```python
def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    counter = False
    odd = dummy_odd = ListNode()
    even = dummy_even = ListNode()
    while head:
        if counter := counter ^ True:
            odd.next = head
            odd = odd.next
        else:
            even.next = head
            even = even.next
        head = head.next

    odd.next = dummy_even.next
    even.next = None
    return dummy_odd.next
```

Explanation: We can use two auxiliary linked list pointers to group all the nodes with odd indices together and the nodes with even indices. After we reach the end of original linked list, we can update the next element of odd pointer as the head of even pointer.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

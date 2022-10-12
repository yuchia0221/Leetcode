# Reverse Nodes in k-Group

Problem can be found in [here](https://leetcode.com/problems/reverse-nodes-in-k-group/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/25-ReverseNodesink-Group/solution.py): Two Pointers

```python
def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    current = head
    new_head = tail = None
    while current:
        count = 0
        current = head
        while count < k and current:
            current = current.next
            count += 1

        if count == k:
            reversed_head = self.reverse_k_nodes(head, k)
            if not new_head:
                new_head = reversed_head
            if tail:
                tail.next = reversed_head

            tail, head = head, current

    if tail:
        tail.next = head
    return new_head if new_head else head

def reverse_k_nodes(self, head: ListNode, k: int) -> ListNode:
    previous_node = None
    while k != 0:
        next_node = head.next
        head.next = previous_node
        previous_node, head = head, next_node
        k -= 1

    return previous_node
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

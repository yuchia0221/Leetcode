# Add Two Numbers II

Problem can be found in [here](https://leetcode.com/problems/add-two-numbers-ii/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/445-AddTwoNumbersII/solution.py)

```python
class Solution:
    def reverse_linked_list(self, node: ListNode) -> ListNode:
        previous_node = None
        while node:
            next_node = node.next
            node.next = previous_node
            node, previous_node = next_node, node

        return previous_node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, l2 = self.reverse_linked_list(l1), self.reverse_linked_list(l2)

        head = None
        carry = 0
        while l1 or l2:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            val = (carry + x1 + x2) % 10
            carry = (carry + x1 + x2) // 10
            current = ListNode(val)
            current.next, head = head, current

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            current = ListNode(carry)
            current.next = head
            head = current

        return head
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>).

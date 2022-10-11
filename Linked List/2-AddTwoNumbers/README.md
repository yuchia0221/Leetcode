# Add Two Numbers

Problem can be found in [here](https://leetcode.com/problems/add-two-numbers/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/2-AddTwoNumbers/solution.py)

```python
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    dummyHead = current = ListNode(0)
    while l1 != None or l2 != None or carry != 0:
        l1_value = l1.val if l1 else 0
        l2_value = l2.val if l2 else 0
        current_sum = l1_value + l2_value + carry
        carry = current_sum // 10
        newNode = ListNode(current_sum % 10)
        current.next = newNode
        current = newNode
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummyHead.next
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

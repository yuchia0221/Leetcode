# Sort List

Problem can be found in [here](https://leetcode.com/problems/sort-list/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/148-SortList/solution.py): Merge Sort

```python

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        start = slow.next
        slow.next = None
        left, right = self.sortList(head), self.sortList(start)
        return self.merge(left, right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if not left or not right:
            return left or right

        dummy_head = previous_node = ListNode(0)
        while left and right:
            if left.val < right.val:
                previous_node.next = left
                left = left.next
            else:
                previous_node.next = right
                right = right.next
            previous_node = previous_node.next
        previous_node.next = left or right

        return dummy_head.next
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

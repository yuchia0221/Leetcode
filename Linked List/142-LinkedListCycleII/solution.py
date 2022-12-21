from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        intersection = self.get_intersect(head)
        if intersection == None:
            return None

        pointer1, pointer2 = head, intersection
        while pointer1 != pointer2:
            pointer1, pointer2 = pointer1.next, pointer2.next

        return pointer1

    def get_intersect(self, head: ListNode) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None

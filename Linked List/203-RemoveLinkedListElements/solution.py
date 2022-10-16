from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
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

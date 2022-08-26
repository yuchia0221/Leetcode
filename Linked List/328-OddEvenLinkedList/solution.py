from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

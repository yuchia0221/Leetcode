from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse_head = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            reverse_head, reverse_head.next, slow = slow, reverse_head, slow.next
        if fast:
            slow = slow.next
        while reverse_head and reverse_head.val == slow.val:
            slow = slow.next
            reverse_head = reverse_head.next

        return not reverse_head

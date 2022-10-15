from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

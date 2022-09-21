from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        memo = defaultdict(int)
        current = head
        while current:
            memo[current.val] += 1
            current = current.next

        dummy = ListNode()
        prev = dummy
        prev.next = head
        current = head
        while current:
            if memo[current.val] == 1:
                prev = current
                current = current.next
            else:
                while current and memo[current.val] != 1:
                    current = current.next
                prev.next = current

        return dummy.next

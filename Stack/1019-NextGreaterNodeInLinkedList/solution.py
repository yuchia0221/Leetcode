from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        index = 0
        answer, stack = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                previous_index = stack.pop()[0]
                answer[previous_index] = head.val

            stack.append((index, head.val))
            answer.append(0)
            head = head.next
            index += 1

        return answer

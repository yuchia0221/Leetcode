# Remove Duplicates From an Unsorted Linked List

Problem can be found in [here](https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/1836-RemoveDuplicatesFromanUnsortedLinkedList/solution.py): Two Pointers + Hash Table

```python
def deleteDuplicatesUnsorted(head: ListNode) -> ListNode:
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
```

Explanation: We can use a two-pass algorithm to solve this problem. In first pass, we need to count the number of occurrences for every value. If it exceeds 2, then we know we should remove it from the linked list. In the second iteration, we remove the duplicated nodes.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>).

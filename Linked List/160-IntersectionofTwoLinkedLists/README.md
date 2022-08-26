# Intersection of Two Linked Lists

Problem can be found in [here](https://leetcode.com/problems/intersection-of-two-linked-lists/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Linked%20List/160-IntersectionofTwoLinkedLists/solution.py): Flag

```python
def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    pointer1, pointer2 = headA, headB
    while pointer1 is not pointer2:
        pointer1 = pointer1.next if pointer1 else headB
        pointer2 = pointer2.next if pointer2 else headA

    return pointer1
```

Explanation: Without modifying the input data, we can perform a two-pass algorithm to solve this problem. The challenge is that since we do not know how many elements in both linked list and which position they intersect. To overcome this problem, we can switch head if we reach the end of the linked list. By doing so, we can compensate the length difference between two linked lists. Also, we will at most iterate both linked lists twice. If there is no intersection, the while loop will stop because two pointers reach $None$. However, two pointers will point to same object and break while loop if there is an intersection.

Time Complexity: ![O(n+m)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+m)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n and m is the length of the linked list $headA$ and $headB$, respectively.

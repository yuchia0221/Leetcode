# Next Greater Node In Linked List

Problem can be found in [here](https://leetcode.com/problems/next-greater-node-in-linked-list/)!

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### [Solution](/Stack/227-BasicCalculatorII/solution.py): Monotonic Stack

```python
def nextLargerNodes(head: Optional[ListNode]) -> List[int]:
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

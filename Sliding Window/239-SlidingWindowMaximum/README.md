# Sliding Window Maximum

Problem can be found in [here](https://leetcode.com/problems/sliding-window-maximum/)!

### [Solution](/Sliding%20Window/239-SlidingWindowMaximum/solution.py): Queue

```python
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    queue = deque()
    output_list = []
    for i, num in enumerate(nums):
        while queue and num >= nums[queue[-1]]:
            queue.pop()
        queue.append(i)

        if queue[0] == i-k:
            queue.popleft()
        if i >= k - 1:
            output_list.append(nums[queue[0]])

    return output_list
```

Explanation: We can use an interesting data structure called monotonic queue to solve this problem. Unlike typical queue, monotonic queue is sorted ascendingly or descendingly. In each iteration, we need to pop up all of the value that is smaller than our current value. By this way, we can constantly check maximum value of our current sliding window in constant time, which is the first element in the queue. Also, we have to check whether the first element exceeds the boundaries of the sliding window and the number of k. If so, we need to pop that value out or push it into our output list.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

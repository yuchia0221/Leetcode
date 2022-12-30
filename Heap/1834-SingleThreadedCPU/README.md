# Single-Threaded CPU

Problem can be found in [here](https://leetcode.com/problems/single-threaded-cpu/)!

### [Solution](/Heap/1834-SingleThreadedCPU/solution.py): Heap + Sorting

```python
def getOrder(tasks: List[List[int]]) -> List[int]:
    sorted_tasks = sorted([enqueue, process, index] for index, (enqueue, process) in enumerate(tasks))

    n = len(sorted_tasks)
    queue, tasks_order = [], []
    current_time = index = 0
    while index < n or queue:
        if not queue and current_time < sorted_tasks[index][0]:
            current_time = sorted_tasks[index][0]

        while index < n and current_time >= sorted_tasks[index][0]:
            _, process, task_index = sorted_tasks[index]
            heappush(queue, (process, task_index))
            index += 1

        process, task_index = heappop(queue)
        current_time += process
        tasks_order.append(task_index)

    return tasks_order
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

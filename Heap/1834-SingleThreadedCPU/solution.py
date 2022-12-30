from heapq import heappop, heappush
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
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

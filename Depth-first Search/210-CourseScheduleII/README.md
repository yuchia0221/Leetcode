# Course Schedule II

Problem can be found in [here](https://leetcode.com/problems/course-schedule-ii/)!

### [Solution](/Depth-first%20Search/210-CourseScheduleII/solution.py): Topological Sort

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        for dest, src in prerequisites:
            self.graph[src].append(dest)

        self.is_possible = True
        self.course_order = []
        self.color = [0 for _ in range(numCourses)]
        for course_num in range(numCourses):
            if self.color[course_num] == 0:
                self.dfs(course_num)

        return self.course_order[::-1] if self.is_possible else []

    def dfs(self, vertex: int):
        if not self.is_possible:
            return

        self.color[vertex] = 1
        for neighbor in self.graph[vertex]:
            if self.color[neighbor] == 0:
                self.dfs(neighbor)
            elif self.color[neighbor] == 1:
                self.is_possible = False
                return

        self.color[vertex] = 2
        self.course_order.append(vertex)
```

Explanation: We can perform topological sort to solve this problem. If there is not a cycle in the traversal, we can have a valid course order. However, if we detect there is a cycle inside the traversal, we will notice there will not be a valid course order.

Time Complexity: ![O(V+E)](<https://latex.codecogs.com/svg.image?\inline&space;O(V+E)>), Space Complexity: ![O(V+E)](<https://latex.codecogs.com/svg.image?\inline&space;O(V+E)>), where V is the number of courses and E is the length of prerequisites.

from collections import defaultdict
from typing import List


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

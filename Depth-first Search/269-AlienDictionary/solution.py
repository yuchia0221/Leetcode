from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        in_degree = defaultdict(int)

        for i in range(len(words)-1):
            for char1, char2 in zip(words[i], words[i+1]):
                if char1 != char2:
                    graph[char1].add(char2)
                    in_degree[char2] += 1
                    break

        alien_dictionary = ""
        zero_incoming_edges = deque([char for char in in_degree if in_degree[char] == 0])
        while zero_incoming_edges:
            vertex = zero_incoming_edges.popleft()
            alien_dictionary += vertex
            for neighbor in graph[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_incoming_edges.append(neighbor)

        return alien_dictionary if len(alien_dictionary) == len(words) else ""

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited_rooms = set([0])
        while stack:
            room_num = stack.pop()
            for neighbor in rooms[room_num]:
                if neighbor not in visited_rooms:
                    stack.append(neighbor)
                    visited_rooms.add(neighbor)

        return len(visited_rooms) == len(rooms)

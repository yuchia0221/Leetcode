# Keys and Rooms

Problem can be found in [here](https://leetcode.com/problems/keys-and-rooms/)!

### [Solution](/Depth-first%20Search/841-KeysandRooms/solution.py): Depth-first Search

```python
def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    stack = [0]
    visited_rooms = set([0])
    while stack:
        room_num = stack.pop()
        for neighbor in rooms[room_num]:
            if neighbor not in visited_rooms:
                stack.append(neighbor)
                visited_rooms.add(neighbor)

    return len(visited_rooms) == len(rooms)
```

Explanation: Perform DFS to solve this problem and skip already visited rooms when encounters the same key to visited rooms.

Time Complexity: ![O(V+E)](<https://latex.codecogs.com/svg.image?\inline&space;O(V+E)>), Space Complexity: ![O(V)](<https://latex.codecogs.com/svg.image?\inline&space;O(V)>), where V and E is the number of rooms and number of keys, respectively.

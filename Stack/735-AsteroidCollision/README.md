# Asteroid Collision

Problem can be found in [here](https://leetcode.com/problems/asteroid-collision/)!

### [Solution](/Stack/735-AsteroidCollision/solution.py): Stack

```python
def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []

    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] + asteroid < 0:
                stack.pop()
            elif stack[-1] == -asteroid:
                stack.pop()
                break
            else:
                break
        else:
            stack.append(asteroid)

    return stack
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

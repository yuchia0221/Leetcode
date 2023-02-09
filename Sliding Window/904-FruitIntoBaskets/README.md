# Fruit Into Baskets

Problem can be found in [here](https://leetcode.com/problems/fruit-into-baskets/)!

### [Solution](/Sliding%20Window/904-FruitIntoBaskets//solution.py): Hash Table + Sliding Window

```python
def totalFruit(fruits: List[int]) -> int:
    left = 0
    basket = defaultdict(int)

    for right in range(len(fruits)):
        basket[fruits[right]] += 1

        if len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

    return len(fruits) - left
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

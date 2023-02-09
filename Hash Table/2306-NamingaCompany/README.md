# Naming a Company

Problem can be found in [here](https://leetcode.com/problems/naming-a-company/)!

### [Solution](/Hash%20Table/2306-NamingaCompany/solution.py): Hash Table

```python
def distinctNames(ideas: List[str]) -> int:
    initial_groups = [set() for _ in range(26)]
    for idea in ideas:
        initial_groups[ord(idea[0])-ord("a")].add(idea[1:])

    answer = 0
    for i in range(25):
        for j in range(i+1, 26):
            num_of_mutual = len(initial_groups[i] & initial_groups[j])
            answer += 2 * (len(initial_groups[i])-num_of_mutual) * (len(initial_groups[j])-num_of_mutual)

    return answer
```

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), where n is the length of array ideas and m is the maximum length of a word in array ideas

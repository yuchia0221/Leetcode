# Analyze User Website Visit Pattern

Problem can be found in [here](https://leetcode.com/problems/analyze-user-website-visit-pattern/)!

### [Solution](/Hash%20Table/1152-AnalyzeUserWebsiteVisitPattern/solution.py): Hash Table

```python
def mostVisitedPattern(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    patterns = Counter()
    user_pattern = defaultdict(list)

    for user, _, site in sorted(zip(username, timestamp, website)):
        user_pattern[user].append(site)

    for user, sites in user_pattern.items():
        patterns.update(set(combinations(sites, 3)))

    return max(sorted(patterns), key=patterns.get)
```

Time Complexity: ![O(n!)](<https://latex.codecogs.com/svg.image?\inline&space;O(n!)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

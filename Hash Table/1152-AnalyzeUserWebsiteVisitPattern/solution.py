from collections import Counter, defaultdict
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patterns = Counter()
        user_pattern = defaultdict(list)

        for user, _, site in sorted(zip(username, timestamp, website)):
            user_pattern[user].append(site)

        for user, sites in user_pattern.items():
            patterns.update(set(combinations(sites, 3)))

        return max(sorted(patterns), key=patterns.get)

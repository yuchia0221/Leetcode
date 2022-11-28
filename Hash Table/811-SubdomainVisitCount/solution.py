from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_visit_counter = defaultdict(int)

        for cpdomain in cpdomains:
            time, domain = cpdomain.split()
            subdomains = domain.split(".")
            domain_visit_counter[domain] += int(time)

            if len(subdomains) == 3:
                domain_visit_counter[".".join(subdomains[1:])] += int(time)
            domain_visit_counter[subdomains[-1]] += int(time)

        return [" ".join([str(time), domain])for domain, time in domain_visit_counter.items()]

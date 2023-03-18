# Design Browser History

Problem can be found in [here](https://leetcode.com/problems/design-browser-history/)!

### [Solution](/Design/1472-DesignBrowserHistory/solution.py)

```python
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = self.last = 0
        
    def visit(self, url: str) -> None:
        self.current += 1
        if len(self.history) > self.current:
            self.history[self.current] = url
        else:
            self.history.append(url)
        
        self.last = self.current

    def back(self, steps: int) -> str:
        self.current = max(0, self.current-steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.last, self.current+steps)
        return self.history[self.current]
```

Time Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the number of function visit calls. 

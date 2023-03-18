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

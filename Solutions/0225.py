class MyStack:

    def __init__(self):
        self.q = collections.deque() # type: ignore

    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(len(self.q) - 1):
            t = self.q.popleft()
            self.q.append(t)
    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return True if not self.q else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
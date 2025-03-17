class MinStack:
    def __init__(self):
        self.stack = []
        self.min_elements = []
        self.min_element = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_element:
            self.min_elements.append(val)
            self.min_element = val

    def pop(self) -> None:
        if self.min_element == self.stack[-1]:
            self.min_elements.pop()
        if self.min_elements:
            self.min_element = self.min_elements[-1]
        else:
            self.min_element = float('inf')
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_elements:
            return self.min_elements[-1]
        return self.stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
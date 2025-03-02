class RecentCounter:

    def __init__(self):
        self.que = []

    def ping(self, t: int) -> int:
        self.que.append(t)
        if len(self.que) < 2:
            return len(self.que)

        while len(self.que) > 1:
            if self.que[-1] - self.que[0] > 3000:
                self.que.pop(0)
            else: 
                break
        return len(self.que) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
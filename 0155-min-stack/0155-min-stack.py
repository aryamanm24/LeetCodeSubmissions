class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    # 12, 9, 6, pop, 20
    # stack = [12, 9, 20]
    # min = [12, 9]
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if(not self.min):
            self.min.append(val)
        # There is some min. val
        else:
            if(val <= self.min[-1]):
                self.min.append(val)
        

    def pop(self) -> None:
        if(self.stack[-1] == self.min[-1]):
            self.min.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
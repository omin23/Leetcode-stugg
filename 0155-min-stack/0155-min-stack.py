class MinStack:

    def __init__(self):
        self.mint = []
        self.nums = []

    def push(self, val: int) -> None:
        if not self.mint:
            self.nums.append(val)
            self.mint.append(val)
            return
        self.nums.append(val)
        self.mint.append(min(self.mint[-1],val))
    
    def pop(self) -> None:
        if self.nums:
            self.nums.pop()
            self.mint.pop()
    
       
    def top(self) -> int:
        return self.nums[-1]
    
    def getMin(self) -> int:
        return self.mint[-1]
       



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
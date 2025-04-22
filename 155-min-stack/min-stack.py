class MinStack:

    def __init__(self):
        
        self.stack=[]
        self.mini=float('inf')
    def push(self, val: int) -> None:
       
        if len(self.stack)==0:
            self.mini=val
            self.stack.append(val)
        else:
            if val>self.mini:
                self.stack.append(val)
            else:
                self.stack.append(2*val-self.mini)
                self.mini=val
    def pop(self) -> None:
        if len(self.stack)==0:
            return
        x=self.stack[-1]
        self.stack.pop()
        if x<self.mini:
            self.mini=2*self.mini-x

    

    def top(self) -> int:
        if len(self.stack)==0:
            return
        x=self.stack[-1]
        if self.mini<x:
            return x
        else:
            return self.mini
        
       
    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s1) + len(self.s2) == 0
"""
s1: 2, 1
s2: 
"""


# Your Mysueue object will be instantiated and called as such:
# obj = Mysueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MyQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        while len(self.q1) != 0:
            self.q2.append(self.q1.pop())
        self.q1.append(x)
        while len(self.q2) != 0:
            self.q1.append(self.q2.pop())

    def pop(self) -> int:
        return self.q1.pop()

    def peek(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0
"""
q1: 2, 1
q2: 
"""


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MinStack:

    def __init__(self):
        self.values = Stack()
        self.min_values = Stack()
        

    def push(self, val: int) -> None:
        if len(self.min_values) == 0 or val <= self.min_values.peek():
            self.min_values.push(val)
        self.values.push(val)
        

    def pop(self) -> None:
        val = self.values.pop()
        if val == self.min_values.peek():
            self.min_values.pop()
        return val
        

    def top(self) -> int:
        return self.values.peek()
        

    def getMin(self) -> int:
        return self.min_values.peek()
        

class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop(-1)
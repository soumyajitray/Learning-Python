class Stack:
    def __init__(self):
        self.stack= []
    def isEmpty (self):
        return self.stack == []
    def push (self, data):
        self.stack.append(data)
    def pop (self):
        top=self.stack[-1]
        del self.stack[-1]
        return top
    def peek (self):
        return self.stack[-1]
    def stacksize(self):
        return len(self.stack)
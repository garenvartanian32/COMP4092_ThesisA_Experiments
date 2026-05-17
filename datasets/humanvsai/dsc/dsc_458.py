class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def mul_last_two(self):
        if self.size() < 2:
            return None
        else:
            a = self.pop()
            b = self.pop()
            return a * b

stack = Stack()
stack.push(2)
stack.push(3)
print(stack.mul_last_two())  # Output: 6
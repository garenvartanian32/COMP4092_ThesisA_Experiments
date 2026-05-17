class MyList:
    def __init__(self):
        self.data = []

    def pop(self, index=-1):
        if not self.data:
            raise StackUnderflowException("Stack is empty")
        return self.data.pop(index)
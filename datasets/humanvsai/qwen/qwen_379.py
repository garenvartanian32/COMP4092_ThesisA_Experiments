def pop(self, index=-1) -> Union[int, Expression]:
    if not self.items:
        raise StackUnderflowException('Cannot pop from an empty stack')
    return self.items.pop(index)
def pop(self, index=-1) -> Union[int, Expression]:
        try:
            return super(MachineStack, self).pop(index)
        except IndexError:
            raise StackUnderflowException("Trying to pop from an empty stack")
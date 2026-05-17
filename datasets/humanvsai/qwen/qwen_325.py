def transition(self, inputSymbol):
    if inputSymbol in self.transitions:
        (nextState, output) = self.transitions[inputSymbol]
        self.state = nextState
        return output
    else:
        raise ValueError(f"No transition defined for input symbol '{inputSymbol}'")
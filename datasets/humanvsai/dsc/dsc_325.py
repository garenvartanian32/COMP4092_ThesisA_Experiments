class StateMachine:
    def __init__(self):
        self.state = 'A'
        self.transitions = {
            'A': {'input1': ('B', 'output1'), 'input2': ('C', 'output2')},
            'B': {'input3': ('A', 'output3'), 'input4': ('C', 'output4')},
            'C': {'input5': ('A', 'output5'), 'input6': ('B', 'output6')},
        }

    def transition(self, inputSymbol):
        if inputSymbol in self.transitions[self.state]:
            self.state, output = self.transitions[self.state][inputSymbol]
            return output
        else:
            raise ValueError('Invalid input symbol')
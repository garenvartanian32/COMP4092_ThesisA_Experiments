def transition(self, inputSymbol):
        outState, outputSymbols = self._automaton.outputForInput(self._state,
                                                                 inputSymbol)
        outTracer = None
        if self._tracer:
            outTracer = self._tracer(self._state._name(),
                                     inputSymbol._name(),
                                     outState._name())
        self._state = outState
        return (outputSymbols, outTracer)
def create_initial(self, address_values):
        with self._lock:
            for add, val in address_values:
                self._state[add] = _ContextFuture(address=add, result=val)
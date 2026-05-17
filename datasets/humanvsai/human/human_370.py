def _send_streamify(self, frame):
        # Get the state and framer
        state = self._send_framer_state
        framer = self._send_framer
        # Reset the state as needed
        state._reset(framer)
        # Now pass the frame through streamify() and return the result
        return framer.streamify(state, frame)
def is_mouse_over(self, event, include_label=True, width_modifier=0):
        # Disabled widgets should not react to the mouse.
        logger.debug("Widget: %s (%d, %d) (%d, %d)", self, self._x, self._y, self._w, self._h)
        if self._is_disabled:
            return False
        # Check for any overlap
        if self._y <= event.y < self._y + self._h:
            if ((include_label and self._x <= event.x < self._x + self._w - width_modifier) or
                    (self._x + self._offset <= event.x < self._x + self._w - width_modifier)):
                return True
        return False
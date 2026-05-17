def is_mouse_over(self, event, include_label=True, width_modifier=0):
    effective_width = self.width + width_modifier
    if event.x >= 0 and event.x <= effective_width and (event.y >= 0) and (event.y <= self.height):
        if include_label and self.label:
            label_width = self.label.width
            if event.x >= 0 and event.x <= label_width:
                return True
            else:
                return event.x > label_width
        else:
            return True
    else:
        return False
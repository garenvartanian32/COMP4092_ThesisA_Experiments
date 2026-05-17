def is_mouse_over(self, event, include_label=True, width_modifier=0):
    # Get the position of the mouse event
    mouse_x, mouse_y = event.pos

    # Get the position and size of the widget
    widget_x, widget_y = self.get_position()
    widget_width, widget_height = self.get_size()

    # Adjust the width if necessary
    widget_width += width_modifier

    # Check if the mouse is over the widget
    if include_label:
        return widget_x <= mouse_x <= (widget_x + widget_width) and widget_y <= mouse_y <= (widget_y + widget_height)
    else:
        # If we're not including the label, we need to adjust the position and size
        label_width, _ = self.get_label_size()
        widget_x += label_width
        widget_width -= label_width
        return widget_x <= mouse_x <= (widget_x + widget_width) and widget_y <= mouse_y <= (widget_y + widget_height)
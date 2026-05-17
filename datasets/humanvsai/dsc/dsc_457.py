def _create_properties(self):
    properties = []
    for widget in self.winfo_children():
        properties.append(widget.cget('text'))  # assuming the property you want is 'text'
    return properties
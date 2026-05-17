def _create_properties(self):
    self.properties_frame = tk.Frame(self.root)
    self.properties_frame.pack(side=tk.TOP, fill=tk.X)
    self.properties_listbox = tk.Listbox(self.properties_frame)
    self.properties_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    self.properties_listbox.bind('<<ListboxSelect>>', self._on_property_select)
    self.properties_scrollbar = tk.Scrollbar(self.properties_frame, orient=tk.VERTICAL)
    self.properties_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    self.properties_listbox.config(yscrollcommand=self.properties_scrollbar.set)
    self.properties_scrollbar.config(command=self.properties_listbox.yview)
    self.properties_listbox.insert(tk.END, *self.editable_properties)

def _on_property_select(self, event):
    """Handle the selection of a property in the listbox"""
    selected_index = self.properties_listbox.curselection()
    if selected_index:
        selected_property = self.properties_listbox.get(selected_index)
        self._display_property_details(selected_property)

def _display_property_details(self, property_name):
    """Display details of the selected property"""
    print(f'Displaying details for {property_name}')
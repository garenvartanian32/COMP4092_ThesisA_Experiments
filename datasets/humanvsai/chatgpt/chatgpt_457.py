def populate_frame(frame, editable_properties):
    for prop in editable_properties:
        prop_label = tkinter.Label(frame, text=prop)
        prop_label.pack()

        prop_entry = tkinter.Entry(frame)
        prop_entry.pack()

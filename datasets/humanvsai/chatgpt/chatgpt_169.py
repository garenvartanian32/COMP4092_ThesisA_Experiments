import os
import selectiontools

def read_network_files():
    network_files = [file for file in os.listdir() if file.endswith('.net')]
    selections = selectiontools.Selections()
    for file in network_files:
        with open(file, 'r') as f:
            contents = f.read()
            selections.add_selection(file, contents)
    return selections

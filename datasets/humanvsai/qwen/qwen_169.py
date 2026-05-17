def load_files(self) -> selectiontools.Selections:
    files = os.listdir('.')
    network_files = [f for f in files if f.endswith('.net')]
    selections = selectiontools.Selections()
    for file in network_files:
        with open(file, 'r') as f:
            content = f.read()
            selection = selectiontools.Selection(content)
            selections.append(selection)
    return selections
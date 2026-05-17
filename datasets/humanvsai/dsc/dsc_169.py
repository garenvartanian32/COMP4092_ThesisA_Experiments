import os
import glob
from selectiontools import Selections

def load_files(self) -> Selections:
    # Get the current working directory
    cwd = os.getcwd()

    # Get all files in the current working directory
    files = glob.glob(os.path.join(cwd, '*'))

    # Create a Selections object
    selections = Selections()

    # Load each file and add its contents to the Selections object
    for file in files:
        with open(file, 'r') as f:
            contents = f.read()
            selections.add(contents)

    return selections
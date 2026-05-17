import os

class MyClass:
    def __init__(self, in_dir):
        self.in_dir = in_dir

    def process_directories(self):
        for root, dirs, files in os.walk(self.in_dir):
            for file in files:
                if file.endswith('.rst'):
                    with open(os.path.join(root, file), 'w') as f:
                        # Here you can write whatever you want into the .rst file
                        f.write('This is a test')
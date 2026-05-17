import pickle

class MyApp:
    def __init__(self):
        self.config = {}

    def save_config(self):
        with open('config.pkl', 'wb') as f:
            pickle.dump(self.config, f, pickle.HIGHEST_PROTOCOL)

    def load_config(self):
        with open('config.pkl', 'rb') as f:
            self.config = pickle.load(f)
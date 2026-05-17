class Client:
    def __init__(self):
        self.selected_language = None

    def select_language(self, language):
        """Store client's selection of a new translation"""
        self.selected_language = language
        print(f"Client's selected language is now {self.selected_language}")

# Usage
client = Client()
client.select_language('English')
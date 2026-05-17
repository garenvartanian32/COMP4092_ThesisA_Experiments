class MyClass:
    def __init__(self):
        self.preferences = {}  # Initialize an empty dictionary to store preferences

    def edit_project_preferences(self, preference_name, preference_value):
        """Edit Spyder active project preferences"""
        self.preferences[preference_name] = preference_value
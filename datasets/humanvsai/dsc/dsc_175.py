class MyClass:
    def __init__(self):
        self.customizations = [
            {'key': 'value'},
            {'key2': 'value2'},
            # Add more customizations as needed
        ]

    def widgets(self):
        """Get the customization from the activity.

        :return: The customization in `list(dict)` form
        """
        return self.customizations
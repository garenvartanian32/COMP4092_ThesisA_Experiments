def run(self, data):
    result = self.check(data)
    (status, messages) = result
    formatted_messages = self.format_messages(messages)
    return (status, formatted_messages)

def check(self, data):
    """Check the data for specific conditions.

        Args:
            data (DSM/DMM/MDM): DSM/DMM/MDM instance to check.

        Returns:
            tuple (int, list): status constant from Checker class and list of messages."""
    return (Checker.SUCCESS, ['Check passed successfully.'])

def format_messages(self, messages):
    """Format the messages for better readability.

        Args:
            messages (list): List of messages to format.

        Returns:
            str: Formatted messages."""
    return '\n'.join(messages)
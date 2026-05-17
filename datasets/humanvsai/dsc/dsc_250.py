def send_data(self, screen_id: int, format_p: str, data: str):
    """Initiates sending data to the target.

    Parameters:
    screen_id (int): The screen ID where the drag and drop event occurred.
    format_p (str): The MIME type the data is in.
    data (str): The actual data.

    Returns:
    IProgress: Progress object to track the operation completion.

    Raises:
    VBoxErrorVmError: VMM device is not available.
    """
    # Your function implementation goes here
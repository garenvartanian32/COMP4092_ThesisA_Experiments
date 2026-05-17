def send_data(screen_id: int, format_p: str, data: str) -> IProgress:
    # code to send data to the target
    progress = IProgress()  # assuming IProgress is already imported or defined
    if not VMM_device_available:
        raise VBoxErrorVmError('VMM device is not available.')
    return progress

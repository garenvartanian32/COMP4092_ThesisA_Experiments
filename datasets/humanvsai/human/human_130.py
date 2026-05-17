def _query_pageant(msg):
    hwnd = _get_pageant_window_object()
    if not hwnd:
        # Raise a failure to connect exception, pageant isn't running anymore!
        return None
    # create a name for the mmap
    map_name = "PageantRequest%08x" % thread.get_ident()
    pymap = _winapi.MemoryMap(
        map_name, _AGENT_MAX_MSGLEN, _winapi.get_security_attributes_for_user()
    )
    with pymap:
        pymap.write(msg)
        # Create an array buffer containing the mapped filename
        char_buffer = array.array("b", b(map_name) + zero_byte)  # noqa
        char_buffer_address, char_buffer_size = char_buffer.buffer_info()
        # Create a string to use for the SendMessage function call
        cds = COPYDATASTRUCT(
            _AGENT_COPYDATA_ID, char_buffer_size, char_buffer_address
        )
        response = ctypes.windll.user32.SendMessageA(
            hwnd, win32con_WM_COPYDATA, ctypes.sizeof(cds), ctypes.byref(cds)
        )
        if response > 0:
            pymap.seek(0)
            datalen = pymap.read(4)
            retlen = struct.unpack(">I", datalen)[0]
            return datalen + pymap.read(retlen)
        return None
def raise_specific_errors(status_code):
    if status_code == 400:
        raise ValueError("Bad Request")
    elif status_code == 401:
        raise PermissionError("Unauthorized")
    elif status_code == 403:
        raise PermissionError("Forbidden")
    elif status_code == 404:
        raise FileNotFoundError("Not Found")
    elif status_code == 406:
        raise ValueError("Not Acceptable")
    elif status_code == 500:
        raise RuntimeError("Internal Server Error")
    else:
        return "No error raised for this status code"

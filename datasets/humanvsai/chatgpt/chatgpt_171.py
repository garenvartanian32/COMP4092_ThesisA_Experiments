def add_uid(uid: str, skip_handle: bool, data: dict) -> dict:
    if not skip_handle:
        data["handle"] = uid
    else:
        data["uid"] = uid
    return data

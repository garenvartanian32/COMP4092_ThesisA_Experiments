def intern_name(name: str, only_if_exists: bool) -> int:
    return sys.intern(name) if only_if_exists else id(name)

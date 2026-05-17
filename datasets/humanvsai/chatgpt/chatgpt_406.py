def build_dict_without_none_fields(d: dict) -> dict:
    return {k: v for k, v in d.items() if v is not None}
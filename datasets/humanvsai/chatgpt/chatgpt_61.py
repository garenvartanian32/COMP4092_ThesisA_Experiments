def remove_keys_for_account(account, key_dict):
    keys_to_remove = []
    for key, value in key_dict.items():
        if value == account:
            keys_to_remove.append(key)
    for key in keys_to_remove:
        del key_dict[key]
    return key_dict

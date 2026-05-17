def restore_tabs():
    last_status = get_last_status()  # assume this function gets the last status of the state machine
    backup_path = get_backup_path()  # assume this function gets the backup path of the state machine
    original_path = get_original_path()  # assume this function gets the original path of the state machine
    
    if last_status in backup_path:
        load_state_machine(last_status, backup_path)
    else:
        load_state_machine(last_status, original_path)

    add_to_recently_opened(original_path)  # assume this function adds the original path to the recently opened list

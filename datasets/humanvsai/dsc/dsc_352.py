def restore_session_from_runtime_config():
    """Restore stored tabs from runtime config

    The method checks if the last status of a state machine is in the backup or in its original path and loads it
    from there. The original path of these state machines are also inserted into the recently opened state machines
    list.
    """
    # Assume we have a list of state machine IDs in the runtime config
    state_machine_ids = get_state_machine_ids_from_runtime_config()

    for state_machine_id in state_machine_ids:
        # Assume we have a function that checks if a state machine is in the backup
        if is_in_backup(state_machine_id):
            # Load the state machine from the backup
            state_machine = load_state_machine(state_machine_id)
        else:
            # Load the state machine from its original path
            state_machine = load_state_machine_from_original_path(state_machine_id)

        # Assume we have a function that inserts a state machine into the recently opened list
        insert_into_recently_opened(state_machine)
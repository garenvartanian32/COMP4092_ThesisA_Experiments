def session(sess_id_or_alias):
    """Show detailed information for a running compute session.

    SESSID: Session id or its alias.
    """
    # Assuming you have a dictionary of sessions where the key is the session id or alias
    # and the value is the session information
    sessions = {
        "sess1": {"id": "sess1", "status": "running", "start_time": "2022-01-01 00:00:00"},
        "alias1": {"id": "sess2", "status": "running", "start_time": "2022-01-01 00:00:00"},
    }

    # Check if the session id or alias exists in the sessions dictionary
    if sess_id_or_alias in sessions:
        session_info = sessions[sess_id_or_alias]
        print(f"Session ID: {session_info['id']}")
        print(f"Status: {session_info['status']}")
        print(f"Start Time: {session_info['start_time']}")
    else:
        print("Session not found")
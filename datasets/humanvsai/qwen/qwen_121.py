def session(sess_id_or_alias):
    pass

def list_sessions():
    """List all running compute sessions."""
    pass

def terminate_session(sess_id_or_alias):
    """Terminate a running compute session.

    SESSID: Session id or its alias."""
    pass

def restart_session(sess_id_or_alias):
    """Restart a running compute session.

    SESSID: Session id or its alias."""
    pass

def scale_session(sess_id_or_alias, num_workers):
    """Scale a running compute session.

    SESSID: Session id or its alias.
    NUM_WORKERS: Number of workers to scale the session to."""
    pass

def get_session_status(sess_id_or_alias):
    """Get the status of a running compute session.

    SESSID: Session id or its alias."""
    pass

def create_session(image_name, num_workers, resources):
    """Create a new compute session.

    IMAGE_NAME: Name of the Docker image to use.
    NUM_WORKERS: Number of workers for the session.
    RESOURCES: Dictionary specifying resource requirements."""
    pass

def update_session(sess_id_or_alias, resources):
    """Update the resources of a running compute session.

    SESSID: Session id or its alias.
    RESOURCES: Dictionary specifying new resource requirements."""
    pass

def get_session_logs(sess_id_or_alias):
    """Get the logs of a running compute session.

    SESSID: Session id or its alias."""
    pass

def get_session_metrics(sess_id_or_alias):
    """Get the metrics of a running compute session.

    SESSID: Session id or its alias."""
    pass

def get_session_config(sess_id_or_alias):
    """Get the configuration of a running compute session.

    SESSID: Session id or its alias."""
    pass
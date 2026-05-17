def dependency_updated(dependency, svc, svc_ref, old_properties, new_value):
    if new_value:
        # Inject the new value of the handler
        dependency.handler = svc
        return "New value injected successfully"
    else:
        return "No new value to inject"

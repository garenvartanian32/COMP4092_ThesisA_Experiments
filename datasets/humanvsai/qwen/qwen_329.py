def update(self, dependency, svc, svc_ref, old_properties, new_value=False):
    if new_value:
        self.inject_new_value(dependency, svc, svc_ref)
    else:
        self.update_properties(dependency, svc, svc_ref, old_properties)

def inject_new_value(self, dependency, svc, svc_ref):
    """Inject the new value of the handler into the service."""
    pass

def update_properties(self, dependency, svc, svc_ref, old_properties):
    """Update the properties of the dependency in the service."""
    pass
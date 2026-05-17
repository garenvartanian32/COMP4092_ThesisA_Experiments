def update(self, dependency, svc, svc_ref, old_properties, new_value=False):
        # type: (Any, Any, ServiceReference, dict, bool) -> None
        with self._lock:
            self.__update_binding(
                dependency, svc, svc_ref, old_properties, new_value
            )
            self.check_lifecycle()
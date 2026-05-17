def _acquire_lock(self, key: str, session_id: str, seconds_to_lock: float, metadata: Any) \
            -> Optional[ConnectedConsulLockInformation]:
        lock_information = ConnectedConsulLockInformation(
            self, key, session_id, datetime.utcnow(), seconds_to_lock, metadata)
        value = json.dumps(lock_information, cls=ConsulLockInformationJSONEncoder, indent=4, sort_keys=True)
        logger.debug(f"Attempting to acquire lock with value: {value}")
        try:
            success = self.consul_client.kv.put(key=key, value=value, acquire=session_id)
        except ConsulException as e:
            if "invalid session" in e.args[0]:
                raise SessionLostConsulError() from e
            raise e
        return lock_information if success else None
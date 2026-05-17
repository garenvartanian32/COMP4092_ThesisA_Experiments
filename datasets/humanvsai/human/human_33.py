def get_diagnosis(self, remediation_id=None):
        if self.config.offline:
            logger.error('Cannot get diagnosis in offline mode.')
            return None
        return self.connection.get_diagnosis(remediation_id)
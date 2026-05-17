def start_accepting_passive_svc_checks(self):
    self.send_command('START_ACCEPTING_PASSIVE_SVC_CHECKS')

def stop_accepting_passive_svc_checks(self):
    """Disable passive service check submission (globally)
        Format of the line that triggers function call::

        STOP_ACCEPTING_PASSIVE_SVC_CHECKS

        :return: None"""
    self.send_command('STOP_ACCEPTING_PASSIVE_SVC_CHECKS')

def start_accepting_passive_host_checks(self):
    """Enable passive host check submission (globally)
        Format of the line that triggers function call::

        START_ACCEPTING_PASSIVE_HOST_CHECKS

        :return: None"""
    self.send_command('START_ACCEPTING_PASSIVE_HOST_CHECKS')

def stop_accepting_passive_host_checks(self):
    """Disable passive host check submission (globally)
        Format of the line that triggers function call::

        STOP_ACCEPTING_PASSIVE_HOST_CHECKS

        :return: None"""
    self.send_command('STOP_ACCEPTING_PASSIVE_HOST_CHECKS')

def send_command(self, command):
    """Send a command to the Nagios server.
        :param command: The command to send
        :return: None"""
    pass
def find_usage(self):
        logger.debug("Checking usage for service %s", self.service_name)
        self.connect()
        for lim in self.limits.values():
            lim._reset_usage()
        resp = self.conn.get_directory_limits()
        directory_limits = resp['DirectoryLimits']
        self.limits['CloudOnlyDirectories']._add_current_usage(
            directory_limits['CloudOnlyDirectoriesCurrentCount'],
            aws_type='AWS::DirectoryService'
        )
        self.limits['CloudOnlyMicrosoftAD']._add_current_usage(
            directory_limits['CloudOnlyMicrosoftADCurrentCount'],
            aws_type='AWS::DirectoryService'
        )
        self.limits['ConnectedDirectories']._add_current_usage(
            directory_limits['ConnectedDirectoriesCurrentCount'],
            aws_type='AWS::DirectoryService'
        )
        self._have_usage = True
        logger.debug("Done checking usage.")
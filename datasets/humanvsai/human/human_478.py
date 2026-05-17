def get_intro_prompt(self):
        server_msg = self.web_services.get_system_status()
        return server_msg + colorize('psiTurk version ' + version_number +
                                     '\nType "help" for more information.',
                                     'green', False)
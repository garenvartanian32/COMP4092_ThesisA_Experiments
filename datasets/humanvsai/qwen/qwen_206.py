def request_will_echo(self):
    self.send_command('WILL ECHO')
    self.telnet.set_option_negotiation_callback(self.handle_echo_option)

def handle_echo_option(self, option, value):
    """Handle the echo option negotiation."""
    if option == self.telnet.ECHO and value == self.telnet.WILL:
        self.telnet.set_option(self.telnet.ECHO, self.telnet.DO)
        self.send_command('DO ECHO')
    elif option == self.telnet.ECHO and value == self.telnet.WONT:
        self.telnet.set_option(self.telnet.ECHO, self.telnet.DONT)
        self.send_command('DONT ECHO')
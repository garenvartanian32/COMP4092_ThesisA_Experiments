def ansi_to_curses(self, char):
    if char == '\x1b':
        self.state = 'ESC'
    elif self.state == 'ESC':
        if char == '[':
            self.state = 'CSI'
        elif char == 'm':
            self.reset_attributes()
        elif char == 'H':
            self.move_cursor_home()
        elif char == 'J':
            self.erase_screen()
        elif char == 'K':
            self.erase_line()
        elif char == 'A':
            self.move_cursor_up()
        elif char == 'B':
            self.move_cursor_down()
        elif char == 'C':
            self.move_cursor_right()
        elif char == 'D':
            self.move_cursor_left()
        else:
            self.state = 'NORMAL'
    elif self.state == 'CSI':
        if char.isdigit():
            self.param += char
        elif char == ';':
            self.params.append(int(self.param))
            self.param = ''
        elif char == 'm':
            self.set_attributes(int(self.param))
            self.params = []
            self.param = ''
            self.state = 'NORMAL'
        elif char == 'H':
            self.move_cursor(int(self.params[0]), int(self.params[1]))
            self.params = []
            self.param = ''
            self.state = 'NORMAL'
        elif char == 'J':
            self.erase_screen(int(self.param))
            self.params = []
            self.param = ''
            self.state = 'NORMAL'
        elif char == 'K':
            self.erase_line(int(self.param))
            self.params = []
            self.param = ''
            self.state = 'NORMAL'
        elif char == 'A':
            self.move_cursor_up(int(self.param))
            self.params = []
            self.param = ''
            self.state = 'NORMAL'
        elif char == 'B':
            self.move_cursor_down(int(self.param))
            self.params = []
            self.param = ''
            self.state = 'NORMAL'
        elif char == 'C':
            self.move_cursor_right(int(self.param))
            self.params = []
            self.param = ''
            self.state = 'NORMAL'
        elif char == 'D':
            self.move_cursor_left(int(self.param))
            self.params = []
            self.param = ''
            self.state = 'NORMAL'
        else:
            self.state = 'NORMAL'
    else:
        self.state = 'NORMAL'
        self.process
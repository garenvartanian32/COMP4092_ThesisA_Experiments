def strip(self, chars=None):
    if chars is None:
        chars = ' \t\n\r\x0b\x0c'
    return self.copy().strip(chars)

def copy(self):
    """Returns a copy of the Colr instance."""
    return Colr(self.text, self.fg, self.bg, self.style)

class Colr:

    def __init__(self, text='', fg=None, bg=None, style=None):
        self.text = text
        self.fg = fg
        self.bg = bg
        self.style = style

    def __str__(self):
        return self.text

    def __repr__(self):
        return f'Colr(text={self.text!r}, fg={self.fg!r}, bg={self.bg!r}, style={self.style!r})'

    def strip(self, chars=None):
        """Strips the specified characters from the text of the Colr instance."""
        if chars is None:
            chars = ' \t\n\r\x0b\x0c'
        self.text = self.text.strip(chars)
        return self

    def copy(self):
        """Returns a copy of the Colr instance."""
        return Colr(self.text, self.fg, self.bg, self.style)
colr_instance = Colr('   Hello, World!   ')
stripped_colr = colr_instance.strip()
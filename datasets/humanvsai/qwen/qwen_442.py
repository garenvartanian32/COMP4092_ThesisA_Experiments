def _get_header(self):
    header = '|'
    for column in self.columns:
        header += f' {column} |'
    header += '\n'
    header += '|'
    for _ in self.columns:
        header += ' --- |'
    header += '\n'
    return header
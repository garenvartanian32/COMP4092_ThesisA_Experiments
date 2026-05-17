def _get_type(self, s):
        # TODO: what if the number is bigger than an int or float?
        if s.startswith('"') and s.endswith('"'):
            return s[1:-1]
        elif s.find('.') != -1: 
            return float(s) 
        else: 
            return int(s)
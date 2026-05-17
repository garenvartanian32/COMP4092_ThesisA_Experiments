class Face:
    def __init__(self, index, name=None):
        self.name = name if name is not None else 'f-' + str(index)
        if index == 0 or index == 'w' or index == 'xm' or index == '-100':
            self.vertices = (0, 4, 7, 3)
        elif index == 1 or index == 'e' or index == 'xp' or index == '100':
            self.vertices = (1, 2, 5, 6)
        elif index == 2 or index == 's' or index == 'ym' or index == '0-10':
            self.vertices = (0, 1, 5, 4)
        elif index == 3 or index == 'n' or index == 'yp' or index == '010':
             self.vertices = (2, 3, 7, 6)
        elif index == 4 or index == 'b' or index == 'zm' or index == '00-1':
            self.vertices = (0, 3, 2, 1)
        elif index == 5 or index == 't' or index == 'zp' or index == '001':
            self.vertices = (4, 5, 6, 7)
        else:
            raise ValueError('Invalid index value')

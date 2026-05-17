def face(self, index, name=None):
        kw_to_index = {
            'w': 0, 'xm': 0, '-100': 0,
            'e': 1, 'xp': 1, '100': 1,
            's': 2, 'ym': 2, '0-10': 2,
            'n': 3, 'yp': 3, '010': 3,
            'b': 4, 'zm': 4, '00-1': 4,
            't': 5, 'zp': 5, '001': 5}
        index_to_vertex = [
            (0, 4, 7, 3),
            (1, 2, 6, 5),
            (0, 1, 5, 4),
            (2, 3, 7, 6),
            (0, 3, 2, 1),
            (4, 5, 6, 7)]
        index_to_defaultsuffix = [
            'f-{}-w',
            'f-{}-n',
            'f-{}-s',
            'f-{}-n',
            'f-{}-b',
            'f-{}-t']
        if isinstance(index, string_types):
            index = kw_to_index[index]
        vnames = tuple([self.vnames[i] for i in index_to_vertex[index]])
        if name is None:
            name = index_to_defaultsuffix[index].format(self.name)
        return Face(vnames, name)
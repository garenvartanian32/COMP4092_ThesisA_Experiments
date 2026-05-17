def get_index_text(self, modname, name_cls):
    if name_cls == 'module':
        return f'{modname} module'
    elif name_cls == 'class':
        return f'{name_cls} {modname}.{name_cls}'
    elif name_cls == 'function':
        return f'{name_cls} {modname}.{name_cls}'
    elif name_cls == 'method':
        return f'{name_cls} {modname}.{name_cls}'
    elif name_cls == 'attribute':
        return f'{name_cls} {modname}.{name_cls}'
    else:
        return f'Unknown object type: {name_cls}'
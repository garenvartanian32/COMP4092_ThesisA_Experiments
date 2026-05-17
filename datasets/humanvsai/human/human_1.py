def get_index_text(self, modname, name_cls):
        if self.objtype.endswith('function'):
            if not modname:
                return _('%s() (built-in %s)') % \
                    (name_cls[0], self.chpl_type_name)
            return _('%s() (in module %s)') % (name_cls[0], modname)
        elif self.objtype in ('data', 'type', 'enum'):
            if not modname:
                type_name = self.objtype
                if type_name == 'data':
                    type_name = 'variable'
                return _('%s (built-in %s)') % (name_cls[0], type_name)
            return _('%s (in module %s)') % (name_cls[0], modname)
        else:
            return ''
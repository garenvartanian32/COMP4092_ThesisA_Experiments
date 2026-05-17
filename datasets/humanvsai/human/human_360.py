def comprehension_walk_newer(self, node, iter_index, code_index=-5):
        p = self.prec
        self.prec = 27
        code = node[code_index].attr
        assert iscode(code), node[code_index]
        code = Code(code, self.scanner, self.currentclass)
        ast = self.build_ast(code._tokens, code._customize)
        self.customize(code._customize)
        # skip over: sstmt, stmt, return, ret_expr
        # and other singleton derivations
        while (len(ast) == 1
               or (ast in ('sstmt', 'return')
                   and ast[-1] in ('RETURN_LAST', 'RETURN_VALUE'))):
            self.prec = 100
            ast = ast[0]
        # Pick out important parts of the comprehension:
        # * the variable we interate over: "store"
        # * the results we accumulate: "n"
        is_30_dict_comp = False
        store = None
        n = ast[iter_index]
        if ast in ('set_comp_func', 'dict_comp_func',
                   'list_comp', 'set_comp_func_header'):
            for k in ast:
                if k == 'comp_iter':
                    n = k
                elif k == 'store':
                    store = k
                    pass
                pass
            pass
        elif ast in ('dict_comp', 'set_comp'):
            assert self.version == 3.0
            for k in ast:
                if k in ('dict_comp_header', 'set_comp_header'):
                    n = k
                elif k == 'store':
                    store = k
                elif k == 'dict_comp_iter':
                    is_30_dict_comp = True
                    n = (k[3], k[1])
                    pass
                elif k == 'comp_iter':
                    n = k[0]
                    pass
                pass
        else:
            assert n == 'list_iter', n
        # FIXME: I'm not totally sure this is right.
        # Find the list comprehension body. It is the inner-most
        # node that is not list_.. .
        if_node = None
        comp_for = None
        comp_store = None
        if n == 'comp_iter':
            comp_for = n
            comp_store = ast[3]
        have_not = False
        while n in ('list_iter', 'comp_iter'):
            # iterate one nesting deeper
            if self.version == 3.0 and len(n) == 3:
                assert n[0] == 'expr' and n[1] == 'expr'
                n = n[1]
            else:
                n = n[0]
            if n in ('list_for', 'comp_for'):
                if n[2] == 'store':
                    store = n[2]
                n = n[3]
            elif n in ('list_if', 'list_if_not', 'comp_if', 'comp_if_not'):
                have_not = n in ('list_if_not', 'comp_if_not')
                if_node = n[0]
                if n[1] == 'store':
                    store = n[1]
                n = n[2]
                pass
            pass
        # Python 2.7+ starts including set_comp_body
        # Python 3.5+ starts including set_comp_func
        # Python 3.0  is yet another snowflake
        if self.version != 3.0:
            assert n.kind in ('lc_body', 'comp_body', 'set_comp_func', 'set_comp_body'), ast
        assert store, "Couldn't find store in list/set comprehension"
        # A problem created with later Python code generation is that there
        # is a lamda set up with a dummy argument name that is then called
        # So we can't just translate that as is but need to replace the
        # dummy name. Below we are picking out the variable name as seen
        # in the code. And trying to generate code for the other parts
        # that don't have the dummy argument name in it.
        # Another approach might be to be able to pass in the source name
        # for the dummy argument.
        if is_30_dict_comp:
            self.preorder(n[0])
            self.write(': ')
            self.preorder(n[1])
        else:
            self.preorder(n[0])
        self.write(' for ')
        if comp_store:
            self.preorder(comp_store)
        else:
            self.preorder(store)
        # FIXME this is all merely approximate
        self.write(' in ')
        self.preorder(node[-3])
        if ast == 'list_comp' and self.version != 3.0:
            list_iter = ast[1]
            assert list_iter == 'list_iter'
            if list_iter == 'list_for':
                self.preorder(list_iter[3])
                self.prec = p
                return
            pass
        if comp_store:
            self.preorder(comp_for)
        elif if_node:
            self.write(' if ')
            if have_not:
                self.write('not ')
            self.preorder(if_node)
            pass
        self.prec = p
def new(self, lits=[], ubound=1, top_id=None):
        self.lits = list(lits)
        self.ubound = ubound
        self.top_id = max(map(lambda x: abs(x), self.lits + [top_id if top_id != None else 0]))
        # saving default SIGINT handler
        def_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_DFL)
        # creating the object
        self.tobj, clauses, self.rhs, self.top_id = pycard.itot_new(self.lits,
                self.ubound, self.top_id)
        # recovering default SIGINT handler
        def_sigint_handler = signal.signal(signal.SIGINT, def_sigint_handler)
        # saving the result
        self.cnf.clauses = clauses
        self.cnf.nv = self.top_id
        # for convenience, keeping the number of clauses
        self.nof_new = len(clauses)
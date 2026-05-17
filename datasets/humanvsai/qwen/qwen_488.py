def new(self, lits=[], ubound=1, top_id=None):
    self.lits = lits
    self.ubound = ubound
    self.top_id = top_id
    self.clauses = []
    self._build_clauses()

def _build_clauses(self):
    """Builds the clauses for the totalizer based on the literals and the upper bound."""
    pass
totalizer = ITotalizer(lits=[1, 2, 3], ubound=5, top_id=10)
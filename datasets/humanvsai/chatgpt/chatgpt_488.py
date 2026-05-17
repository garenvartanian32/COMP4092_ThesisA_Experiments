class ITotalizer:
    def __init__(self, literals, max_bound, top):
        self.literals = literals
        self.max_bound = max_bound
        self.top = top
        self.m = -1
        for lit in self.literals:
            self.m = max(self.m, abs(lit))
        self.counts = [0] * (self.m + 1)
        for lit in self.literals:
            self.counts[abs(lit)] += 1
        self.sizes = []
        for i in range(self.m + 1):
            sz = self.counts[i] + 1
            if sz > 1:
                self.sizes.append(sz)
        self.lits = []
        self.wlits = []
        self.weights = []
        self.nwaux = 0
        for i in range(len(self.sizes)):
            sz = self.sizes[i]
            lits = [0] * sz
            weights = [0] * sz
            for j in range(sz - 1):
                self.nwaux += 1
                lits[j] = self.top + self.nwaux
                weights[j] = 1 << (j + 1)
            lits[sz - 1] = -self.literals[i]
            weights[sz - 1] = 1 << 0
            self.lits.append(lits)
            self.weights.append(weights)
            self.wlits += lits[:-1]
        self.top += self.nwaux

    def attach(self, solver):
        s = 0
        for i in range(len(self.lits)):
            if self.sizes[i] > 1:
                lits = self.lits[i]
                solver.add_clause([lits[-1]])
                for j in range(len(lits) - 1):
                    solver.add_clause([-lits[j], lits[-1]])
                    for k in range(j):
                        solver.add_clause([-lits[k], lits[j]])
                        s += 1
        self.s = s

    def count(self, model):
        count = 0
        for i in range(len(self.lits)):
            s = 0
            for j in range(self.sizes[i] - 1):
                if model[self.lits[i][j]]:
                    s += self.weights[i][j]
            if s >= self.max_bound:
                count += 1
        return count

def solve(self, grid):
        soln = self.S.satisfy_one(assumptions=self._parse_grid(grid))
        return self.S.soln2point(soln, self.litmap)
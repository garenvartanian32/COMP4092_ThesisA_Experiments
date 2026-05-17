def _check_range_minions(self, expr, greedy):
    # Assuming minions is a list of minions
    minions = self.get_minions()
    minions_in_range = []

    for minion in minions:
        if minion.is_in_range(expr):
            minions_in_range.append(minion)
            if not greedy:
                break

    return minions_in_range
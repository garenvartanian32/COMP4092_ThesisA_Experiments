def _iter_categorized_partners(self, state):
    for partner in self.partners:
        if partner.state == state:
            yield (partner, [p for p in self.partners if p.category == partner.category and p.state == state])
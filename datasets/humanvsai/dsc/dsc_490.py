def _iter_categorized_partners(self, state):
    """Iterator over the partners giving as extra param partners of the same
        category."""
    for partner in self.partners:
        if partner.category == state.category:
            yield partner
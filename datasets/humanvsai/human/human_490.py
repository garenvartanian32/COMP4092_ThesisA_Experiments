def _iter_categorized_partners(self, state):
        # categorize partners into the structure
        # partner_class -> list of its instances
        categorized = dict()
        for partner in state.descriptor.partners:
            category, index = categorized.get(partner.__class__,
                                              (list(), len(categorized)))
            category.append(partner)
            categorized[partner.__class__] = tuple([category, index])
        for category, (brothers, index) in sorted(categorized.items(),
                                                  key=lambda x: x[1][1]):
            for partner in brothers:
                yield partner, brothers